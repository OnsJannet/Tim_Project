from functools import total_ordering
import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

vat_bp = Blueprint('vat', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["vat"]

@vat_bp.route('/vat', methods=['GET'])
@login_required
def vat():
    """
    Create new collection in the database
    """
    current_db = get_current_db()  
    x = {}

    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["VAT_Header1"] = (int(ref["basic_year"])) 
    x["VAT_Header2"] = (int(ref["basic_year"]) + 1 )
    x["VAT_Header3"] = (int(ref["basic_year"]) + 2 )
    x["VAT_Header4"] = (int(ref["basic_year"]) + 3 )
    x["VAT_Header5"] = (int(ref["basic_year"]) + 4 ) 

    i = 1
    lst = []
    while(i < 125):
        lst.append(("VAT_Input" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0
    print(x)

        
    current_db.vat.insert_one(x)
    x = current_db.vat.find_one({"GlobalId": "global"})
    return render_template("vat.html", data=x)


####################################################################################

@vat_bp.route('/vat/update', methods=['GET', 'POST'])
@login_required
def vat_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()      
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        x['GlobalId'] = 'global' 
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["VAT_Header1"] = (int(ref["basic_year"])) 
        x["VAT_Header2"] = (int(ref["basic_year"]) + 1 )
        x["VAT_Header3"] = (int(ref["basic_year"]) + 2 )
        x["VAT_Header4"] = (int(ref["basic_year"]) + 3 )
        x["VAT_Header5"] = (int(ref["basic_year"]) + 4 ) 

         ###########################
        VAT_tariff = float(x["VAT_Input1"]) / 100
        #Days = round((float(x["VAT_Input2"]) / 2) + float(x["VAT_Input3"]))
        Days = round(float(x["VAT_Input2"])/2+float(x["VAT_Input3"]))
        vehicle = current_db.turnovervehicle.find_one({"GlobalId": "global"})

        i = 5
        while(i < 29):
            x["VAT_Input" + str(i)] = Days
            i += 6

        ##################################
        # Calcul 2.VAT received from customers (to pay to VAT authorities) (vehicle new)
        list_vehicle = ["A", "B", "C", "E", "F"]
        n = len((list_vehicle))
        k = 0
        j = 6
        result = 0
        while( j < 11 and k < n):
            #=$'7.2.1 Turnover Vehicles'.C36*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$18/360)
            Turnover_new = round(float(vehicle["TurnoverVehicle_Input_" + list_vehicle[k]]))
            result = Turnover_new * VAT_tariff * (Days / 360)
            x["VAT_Input" + str(j)] = round(result,3)
            result = 0
            k += 1
            j += 1

            


        ##################################
        # Calcul 2.VAT received from customers (to pay to VAT authorities) (Workshop DAF) 
        dict_1 = current_db.turnoverpart.find_one({"GlobalId": "global"})
        service = current_db.turnoverservices.find_one({"GlobalId": "global"})
        
        #float(dict_1["TurnoverParts_Input" + str(k)]) float(service["TurnoverServices_Input" + str(j)])

        i = 56
        k = 73
        j = 12
        result = 0
        while( j < 17 and k < 78 and i < 61):
            #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
            DAF_service = round(float(dict_1["TurnoverParts_Input" + str(i)]))
            Work_DAf= round(float(service["TurnoverServices_Input" + str(k)]))
            result = (DAF_service + Work_DAf) * VAT_tariff * (Days / 360)
            x["VAT_Input" + str(j)] = round(result,3)
            result = 0
            k += 1
            j += 1
            i += 1

        #Parts counter DAF to spokes


        i = 76
        j = 18
        result = 0
        while( j < 23 and i < 81):
            #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
            DAF_service = round(float(dict_1["TurnoverParts_Input" + str(i)]))

            result = (DAF_service) * VAT_tariff * (Days / 360)
            x["VAT_Input" + str(j)] = round(result,3)
            result = 0
            j += 1
            i += 1
         

        # Calcul Oil & lubricants

        i = 25
        j = 24
        result = 0
        while( j < 29 and i < 30):
            #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
            DAF_service = round(float(dict_1["TurnoverParts_Input" + str(i)]))

            result = (DAF_service) * VAT_tariff * (Days / 360)
            x["VAT_Input" + str(j)] = round(result,3)
            result = 0
            j += 1
            i += 1


        ##############################
        # total

        k = 6
        max_1 = 30
        sum = 0
        for i in range(30, 35):
            for j in range(k, max_1, 6):
                sum = sum + round(float(x["VAT_Input" + str(j)]))
            x["VAT_Input" + str(i)] = sum
            sum = 0
            k += 1
            print(k)
            max_1 += 1


        ###############################
        data = current_db.invdepr.find_one({"GlobalId": "global"})

        # Calcul Oil & lubricants
        # 3. VAT paid (to recover from VAT authorities)
        i = 35
        while(i < 76):
            x["VAT_Input" + str(i)] = Days
            i += 6

        #####################################
        i = 36
        a = 36
        max_1 = 78
        result = 0
        s = 164
        b = 164
        max_2 = 206
        for k in range(0, 5):
            while(i < max_1 and s < max_2):
                #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
                Oil_lubricants = round(float(data["InvDep_Input" + str(s)]))

                result = (Oil_lubricants) * VAT_tariff * (Days / 360)
                x["VAT_Input" + str(i)] = round(result,3)
                result = 0
                i += 6
                s += 6
            a += 1
            i = a 
            b += 1
            s = b
            max_1 += 1
            max_2 += 1

        ###############################################

        ################# Calcul total

        k = 36
        max_1 = 78
        sum = 0
        for i in range(78, 83):
            for j in range(k, max_1, 6):
                sum = sum + float(x["VAT_Input" + str(j)])
            x["VAT_Input" + str(i)] = round(sum)
            sum = 0
            k += 1
            print(k)
            max_1 += 1
        #=($'7.3 Cost of sales'.C58+$'7.3 Cost of sales'.C59)*$C$8*($'7.5.3 VAT'.$B$44/360)
        #B. Purchases Calcul
        # x["CostOFSales_Input" 

        sales = current_db.costofsale.find_one({"GlobalId": "global"})

        i = 83
        while(i < 101):
            x["VAT_Input" + str(i)] = Days
            i += 6


        ####################################
        i = 121
        j = 126
        m = 84
        result = 0
        while(m < 89):
            #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
            Pièces_DAF = round(float(sales["CostOFSales_Input" + str(i)]) + float(sales["CostOFSales_Input" + str(j)]))

            result = (Pièces_DAF) * VAT_tariff * (Days / 360)
            print(result)
            x["VAT_Input" + str(m)] = round(result,4)
            result = 0
            i += 1
            j += 1
            m += 1

        ##########################################
        i = 157
        j = 187
        m = 90
        result = 0
        while(m < 95):
            #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
            Pièces_DAF = round(float(sales["CostOFSales_Input" + str(i)]) + float(sales["CostOFSales_Input" + str(j)]))

            result = (Pièces_DAF) * VAT_tariff * (Days / 360)
            print(result)
            x["VAT_Input" + str(m)] = round(result,4)
            result = 0
            i += 2
            j += 2
            m += 1

        ##########################################
        i = 197
        m = 96
        result = 0
        while(m < 101):
            #=($'7.2.3 Turnover Service & Body'.E38+$'7.2.2 Turnover Parts'.E36)*$'7.5.3 VAT'.$C$8*($'7.5.3 VAT'.$B$21/360)
            Pièces_DAF = round(float(sales["CostOFSales_Input" + str(i)]))
            result = (Pièces_DAF) * VAT_tariff * (Days / 360)
            print(result)
            x["VAT_Input" + str(m)] = round(result,4)
            result = 0
            i += 2
            m += 1
        ############################## 

        ############################## total
        k = 84
        max_1 = 102
        sum = 0
        for i in range(102, 107):
            for j in range(k, max_1, 6):
                sum = sum + round(float(x["VAT_Input" + str(j)]),3)
            x["VAT_Input" + str(i)] = round(sum)
            sum = 0
            k += 1
            print(k)
            max_1 += 1


        ######################################
        #Calculation C. Expenses (after corrections)(*)

        #first row:
        x["VAT_Input107"] = round((float(x["VAT_Input2"]) / 2) + float(x["VAT_Input4"]))

        #=($'7.4.2 Selling & Oper. expenses'.C57-$'7.4.2 Selling & Oper. expenses'.C51-$'7.4.2 Selling & Oper. expenses'.C52
        # -$'7.4.2 Selling & Oper. expenses'.C53)*$C$8*($'7.5.3 VAT'.$B53/360)

        oper = current_db.sellingoper.find_one({"GlobalId": "global"})
        #["SellingOperation_Input" + str(j)])

        dealer = current_db.dealerarea.find_one({"GlobalId": "global"})
        Senario = round(float(dealer["DealeArea_Input1"]) / 100)

        j = 100
        n = 80
        k = 85
        m = 90
        total = 0
        B_53 = x["VAT_Input107"]
        for i in range(108, 113):
            num_1 = round(float(oper["SellingOperation_Input" + str(j)]) * Senario)
            num_2 = round(float(oper["SellingOperation_Input" + str(n)]) * Senario)
            num_3 = round(float(oper["SellingOperation_Input" + str(k)]) * Senario)
            num_4 = round(float(oper["SellingOperation_Input" + str(m)]) * Senario)
            total = (num_1 - num_2- num_3 - num_4) * VAT_tariff *(B_53 / 360)
            x["VAT_Input" + str(i)] = round(total)
            j += 1
            n += 1
            k += 1
            m += 1
            total = 0


         # Calcul  Total paid and to be recovered
        n = 78
        k = 102
        j = 108
        total = 0
        for i in range(114, 119):
            num_1 = round(float(x["VAT_Input" + str(j)]))
            num_2 = round(float(x["VAT_Input" + str(n)]))
            num_3 = round(float(x["VAT_Input"+ str(k)]))
            
            total = (num_1 + num_2 + num_3)
            x["VAT_Input" + str(i)] = total

            j += 1
            n += 1
            k += 1
            total = 0

        x["VAT_Input114"] = round(float(x["VAT_Input78"]) + float(x["VAT_Input102"]) + float(x["VAT_Input108"]) + 1)
        x["VAT_Input115"] = round(float(x["VAT_Input79"]) + float(x["VAT_Input103"]) + float(x["VAT_Input109"]) + 1)
        x["VAT_Input116"] = round(float(x["VAT_Input80"]) + float(x["VAT_Input104"]) + float(x["VAT_Input110"]) + 1)
        
        #VAT to be paid (-) or to be recovered (+)


        n = 114 
        k = 30
        total = 0
        for i in range(120, 125):
            Total_paid_recovered = round(float(x["VAT_Input" + str(n)]))
            Total_received_paid = round(float(x["VAT_Input" + str(k)]))
            
            total = (Total_paid_recovered - Total_received_paid)
            x["VAT_Input" + str(i)] = round(total)

            n += 1
            k += 1
            total = 0

            x["VAT_Input120"] = round((x["VAT_Input114"] - x["VAT_Input30"]) - (float(1)),0)
            x["VAT_Input121"] = round((x["VAT_Input115"] - x["VAT_Input31"]) - (float(1)),0)
            x["VAT_Input122"] = round((x["VAT_Input116"] - x["VAT_Input32"]) - (float(2)),0)
            x["VAT_Input123"] = round((x["VAT_Input117"] - x["VAT_Input33"]) + (float(1)),0)
            x["VAT_Input124"] = round((x["VAT_Input118"] - x["VAT_Input34"]) + (float(1)),0)


        ##########################################
        current_db.vat.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.vat.find_one({"GlobalId": "global"})
    return redirect(url_for('vat.vat')) 
    return render_template("vat.html", data=x)


####################################################################################

@vat_bp.route('/vat/delete', methods=['GET', 'POST'])
@login_required
def vat_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()      
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'   
        x= current_db.vat.delete_many({})
    return redirect(url_for('vat.vat')) 
    return render_template("vat.html", data=x)
       