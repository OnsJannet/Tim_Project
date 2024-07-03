import imp
from re import A, S
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

costofsale_bp = Blueprint('costofsale', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["costofsale"]

@costofsale_bp.route('/costofsale', methods=['GET'])
@login_required
def costofsale():
    """
    Create new collection in the database
    """    
    
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i < 306):
        lst.append(("CostOFSales_Input" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x)   

    ref = current_db.company.find_one({"GlobalId": "global"})

    x["CostOFSales_Header1"] = (int(ref["basic_year"])) 
    x["CostOFSales_Header2"] = (int(ref["basic_year"]) + 1 )
    x["CostOFSales_Header3"] = (int(ref["basic_year"]) + 2 )
    x["CostOFSales_Header4"] = (int(ref["basic_year"]) + 3 )
    x["CostOFSales_Header5"] = (int(ref["basic_year"]) + 4 )                                     

    current_db.costofsale.insert_one(x)
    x = current_db.costofsale.find_one({"GlobalId": "global"})
    return render_template("cost-of-sales.html", data=x)     



####################################################################################

@costofsale_bp.route('/costofsale/update', methods=['POST'])
@login_required
def costofsale_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global' 
        

        data = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        dict_1 = current_db.turnoverservices.find_one({"GlobalId": "global"})
        dict_2 = current_db.turnoverpart.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["CostOFSales_Header1"] = (int(ref["basic_year"])) 
        x["CostOFSales_Header2"] = (int(ref["basic_year"]) + 1 )
        x["CostOFSales_Header3"] = (int(ref["basic_year"]) + 2 )
        x["CostOFSales_Header4"] = (int(ref["basic_year"]) + 3 )
        x["CostOFSales_Header5"] = (int(ref["basic_year"]) + 4 )   

        ##########################################################
        #Gross margin (of turnover) & average purchase cost per vehicle excluding accessories & bodies mounted by dealer
        #Retail(=(1-$B28)*$'7.2.1 Turnover Vehicles'.C10-($'7.2.3 Turnover Service & Body'.$B$24*$'7.2.3 Turnover Service & Body'.C$34)
        # -$'7.2.2 Turnover Parts'.$B$26)

        # =(1-$B28)*$'7.2.1 Turnover Vehicles'.C10-($'7.2.3 Turnover Service & Body'.$B$24*$'7.2.3 Turnover Service & Body'.C$34)
        # -$'7.2.2 Turnover Parts'.$B$26

        j = 1
        a = 1
        k = 1
        b = 1
        m = 2
        c = 2
        n = 63
        max_1 = 61
        max_2 = 62
        max_3 = 55
        result = 0
        Senario = round(float(dict_1["TurnoverServices_Input16"])) / 100
        num_4 = round(float( dict_2["TurnoverParts_Input35"]))
        service = round(float(dict_1["TurnoverServices_Input37"]))
        for i in range(0, 5):
            while(j < max_1 and m < max_2 and k < max_3):
                num_1 = (round(float(x["CostOFSales_Input" + str(j)]), 1)) * Senario
                num_2 = round(float(data["TurnoverVehicle_Input" + str(k)]))
                num_3 = (service) * round(float(dict_1["TurnoverServices_Input" + str(n)]))
                result = ((1 - (num_1 / 100)) *  num_2) - (num_3) - num_4
                x["CostOFSales_Input" + str(m)] = round(result)
                j += 10
                m += 10
                k += 9
            result = 0
            a = a + 2
            b = b + 2
            c = c + 2
            j = a
            k = b
            m = c
            print(m)
            n += 1
            max_1 += 2
            max_2 += 2
            max_3 += 2

    
    ##################################################################""
        j = 61
        a = 61
        k = 56
        b = 56
        m = 62
        c = 62
        n = 63
        max_1 = 121
        max_2 = 112
        max_3 = 86
        result = 0
        Senario = round(float(dict_1["TurnoverServices_Input16"]) / 100)
        num_4 = round(float( dict_2["TurnoverParts_Input35"]))
        service = round(float(dict_1["TurnoverServices_Input37"]))
        for i in range(0, 5):
            while(j < max_1 and m <= max_2 and k < max_3):
                num_1 = (round(float(x["CostOFSales_Input" + str(j)]), 1) / 100 ) * Senario
                num_2 = round(float(data["TurnoverVehicle_Input" + str(k)]))
                num_3 = (service) * round(float(dict_1["TurnoverServices_Input" + str(n)]))
                result = ((1 - num_1) *  num_2) - (num_3) - num_4
                x["CostOFSales_Input" + str(m)] = round(result)
                print("hello{}".format(j))
                j += 10
                m += 10
                k += 5
            result = 0
            a = a + 2
            b = b + 2
            c = c + 2
            j = a
            k = b
            m = c
            n += 1
            max_1 += 2
            max_2 += 2
            max_3 += 2

        ##################################"
        # Calcul 1.4. Total cost of sales vehicles (New)
        # =($'7.1 Dealer area'.C39-$'7.1 Dealer area'.C51)*$'7.3 Cost of sales'.C28
        # +($'7.1 Dealer area'.C40-$'7.1 Dealer area'.C52)*$'7.3 Cost of sales'.C29
        # +($'7.1 Dealer area'.C43-$'7.1 Dealer area'.C53)*$'7.3 Cost of sales'.C30
        # +($'7.1 Dealer area'.C44-$'7.1 Dealer area'.C54)*$'7.3 Cost of sales'.C31
        # +($'7.1 Dealer area'.C45-$'7.1 Dealer area'.C55)*$'7.3 Cost of sales'.C32
        # +($'7.1 Dealer area'.C46-$'7.1 Dealer area'.C56)*$'7.3 Cost of sales'.C33

        dealer = current_db.dealerarea.find_one({"GlobalId": "global"})

        i = 48
        a = 48
        j = 133
        b = 133
        max_1 = 123
        max_2 = 193
        k = 2
        c = 2
        max_3 = 62
        sum = 0
        for m in range(121,126):
            while(i < max_1 and j < max_2 and k < max_3):
                num_1 = round(float(dealer["DealeArea_Input" + str(i)]))
                num_2 = round(float(dealer["DealeArea_Input" + str(j)]))
                num_3 = round(float(x["CostOFSales_Input" + str(k)]))
                sum = sum + ((num_1 - num_2) * num_3)
                if i == 58 or i == 60 or i == 62 or i == 64 or i == 66:
                    i += 25
                else:
                    i += 10
                j += 10
                k += 10
            x["CostOFSales_Input" + str(m)] = round(sum)
            sum = 0
            a = a + 2
            b = b + 2
            c = c + 2
            i = a
            j = b
            k = c
            max_1 += 2
            max_2 += 2
            max_3 += 2

    #######Calculation fleet (total)
    #=$'7.1 Dealer area'.C51*$'7.3 Cost of sales'.C36
    # +$'7.1 Dealer area'.C52*$'7.3 Cost of sales'.C37
    # +$'7.1 Dealer area'.C53*$'7.3 Cost of sales'.C38
    # +$'7.1 Dealer area'.C54*$'7.3 Cost of sales'.C39
    # +$'7.1 Dealer area'.C55*$'7.3 Cost of sales'.C40
    # +$'7.1 Dealer area'.C56*$'7.3 Cost of sales'.C41
        j = 133
        b = 133
        max_2 = 193
        k = 62
        c = 62
        max_3 = 122
        sum = 0
        for m in range(126,131):
            while(j < max_2 and k < max_3):
                num_2 = round(float(dealer["DealeArea_Input" + str(j)]))
                num_3 = round(float(x["CostOFSales_Input" + str(k)]))
                sum = sum + (num_2 * num_3)
                j += 10
                k += 10
            x["CostOFSales_Input" + str(m)] = round(sum)
            sum = 0
            b = b + 2
            c = c + 2
            j = b
            k = c
            max_2 += 2
            max_3 += 2

        ###########################################
        #Calculation total(new + fleet)

        j = 121
        k = 126
        for i in range(131, 136):
            x["CostOFSales_Input" + str(i)] = round(float(x["CostOFSales_Input" + str(j)])) + round(float(x["CostOFSales_Input" + str(k)]))
            j += 1
            k += 1

        
        # Calculation 1.5. Annual bonus, DAF and other activities

        j = 136
        k = 121
        for i in range(137, 147, 2):
            x["CostOFSales_Input" + str(i)] = round(((float(x["CostOFSales_Input" + str(j)]) / 100)  * float(x["CostOFSales_Input" + str(k)])))
            j += 2
            k += 2

        ###############################################
        # Calculation 2.1. Gross margin (after discount given to the customer) and purchase costs parts (excluding bonus)

        j = 156
        k = 157
        s = 36
        m = 56
        max_1 = 165
        max_2 = 167
        max_3 = 41
        max_4 = 61
        result = 0
        while(j < max_1 and k < max_2 and s < max_3 and m < max_4):
            #=($'7.2.2 Turnover Parts'.C36-$'7.2.2 Turnover Parts'.C26)*(1-$'7.3 Cost of sales'.$B76)
            Workshop_DAF_vehicles = float( dict_2["TurnoverParts_Input" + str(m)])
            Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
            s += 1
            Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
            #Calcul
            result = round((Workshop_DAF_vehicles - Parts_new_trucks) * (1 - Gross_margin))
            m += 1
            j += 2
            x["CostOFSales_Input" + str(k)] = round(result)
            result = 0
            k += 2
    
        """# Calculation second row
        j = 166
        k = 167
        #s = 37
        m = 56
        max_1 = 176
        max_2 = 177
        #max_3 = 401
        max_4 = 66
        result = 0
        while(j < max_1 and k < max_2 and m < max_4):
            #=($'7.2.2 Turnover Parts'.C36-$'7.2.2 Turnover Parts'.C26)*(1-$'7.3 Cost of sales'.$B76)
            Workshop_DAF_vehicles = float( dict_2["TurnoverParts_Input" + str(m)])
            #Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
            Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
            #Calcul
            result = round((Workshop_DAF_vehicles) * (1 - Gross_margin))
            m += 1
            j += 2
            x["CostOFSales_Input" + str(k)] = result
            result = 0
            k += 2"""

        # Calculation others row
        j = 176
        a = 176
        k = 177
        b = 177
        #s = 37
        m = 37
        c = 37
        max_1 = 206
        max_2 = 207
        #max_3 = 401
        max_4 = 91
        result = 0
        for i in range(0, 4):
            while(j < max_1 and k < max_2 and m < max_4):
            #=($'7.2.2 Turnover Parts'.C36-$'7.2.2 Turnover Parts'.C26)*(1-$'7.3 Cost of sales'.$B76)
                Workshop_DAF_vehicles = float( dict_2["TurnoverParts_Input" + str(m)])
            #Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
                Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
            #Calcul
                result = round((Workshop_DAF_vehicles) * (1 - Gross_margin))
                if m == 36 or m == 37 or m == 38 or m == 39 or m == 40:
                    m += 40
                else:
                    m += 5
                j += 10
                if j == 197:
                    m = 25
                elif j == 199:
                    m = 26
                elif j == 199:
                    m = 27
                elif j == 201:
                    m = 28
                elif j == 203:
                    m = 29
                elif j == 205:
                    m = 30
                x["CostOFSales_Input" + str(k)] = round(result)
                result = 0
                k += 10
                print(k)
            a = a + 2
            j = a 
            b = b + 2
            k = b
            c = c + 1
            m = c
            max_1 += 2
            max_2 += 2
            max_4 += 1

        """############### Calculation row (other activities)
         # Calculation second row
        j = 1860
        k = 1870
        #s = 37
        m = 86
        max_1 = 1960
        max_2 = 1970
        #max_3 = 401
        max_4 = 66
        result = 0
        while(j < max_1 and k < max_2 and m < 91):
            #=($'7.2.2 Turnover Parts'.C36-$'7.2.2 Turnover Parts'.C26)*(1-$'7.3 Cost of sales'.$B76)
            Workshop_DAF_vehicles = float( dict_2["TurnoverParts_Input" + str(m)])
            #Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
            Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
            #Calcul
            result = round((Workshop_DAF_vehicles) * (1 - Gross_margin))
            m += 1
            j += 20
            x["CostOFSales_Input" + str(k)] = result
            result = 0
            k += 20"""
        #Calcul last row

        m = 40
        j = 184
        k = 185


        while(j < 214 and k < 215 and m < 500):
            #=($'7.2.2 Turnover Parts'.C36-$'7.2.2 Turnover Parts'.C26)*(1-$'7.3 Cost of sales'.$B76)
                Workshop_DAF_vehicles = float( dict_2["TurnoverParts_Input" + str(m)])
            #Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
                Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
            #Calcul
                result = round((Workshop_DAF_vehicles) * (1 - Gross_margin))
                m += 5
                j += 10
                x["CostOFSales_Input" + str(k)] = round(result)
                result = 0
                k += 10
        # Calcul 1.5. Annual bonus, DAF and other activities (first row)
        i = 236
        j = 226
        k = 157
        a = 157
        m = 237
        max_1 = 246
        max_2 = 236
        max_3 = 247
        max_4 = 197
        sum = 0
        while(i < max_1 and j < max_2 and m < max_3):
            #=(C76+C78+C80+C81)*C88*B91
            Average_bonus = float(x["CostOFSales_Input" + str(i)]) / 100
            Stock_order_percentage_DAF = float(x["CostOFSales_Input" + str(j)]) / 100
            while(k < max_4):
                sum = sum + float(x["CostOFSales_Input" + str(k)])
                if k == 157 or k == 159 or k == 161 or k == 163 or k == 165:
                    k += 20
                else:
                    k += 10
            x["CostOFSales_Input" + str(m)] = round(sum * Average_bonus * Stock_order_percentage_DAF)
            i += 2
            j += 2
            m += 2
            sum = 0
            max_4 += 2
            a = a + 2
            k = a

       # Calcul 1.5. Annual bonus, DAF and other activities (second row)
        """i = 246
        k = 167
        a = 157
        m = 247
        s = 1870
        b = 197
        max_1 = 256
        max_3 = 257
        max_4 = 1970
        sum = 0
        while(i < max_1 and m < max_3):
            #=(C76+C78+C80+C81)*C88*B91
            Average_bonus = float(x["CostOFSales_Input" + str(i)]) / 100
            sum = float(x["CostOFSales_Input" + str(k)]) + float(x["CostOFSales_Input" + str(s)]) + float(x["CostOFSales_Input" + str(b)])
            x["CostOFSales_Input" + str(m)] = round(sum * Average_bonus)
            i += 2
            m += 2
            k += 2
            s += 20
            b += 2
            sum = 0"""
                
        #####################################################
        # Calcul 3. Outsourced workshop activities: gross margin (of turnover) & cost of sales
        i = 257
        j = 267
        k = 256
        s = 88
        result = 0
        while(i < 267 and j < 277 and k < 266 and s < 93):
            num_1= float(dict_1["TurnoverServices_Input" + str(s)])
            Gross_margin  = float(x["CostOFSales_Input" + str(k)]) / 100
            #=$'7.2.3 Turnover Service & Body'.C49*(1-$'7.3 Cost of sales'.$B$99)
            result = round(num_1 * ( 1 - Gross_margin), 3)
            x["CostOFSales_Input" + str(i)] = round(result)
            x["CostOFSales_Input" + str(j)] = round(result)
            result = 0
            i += 2
            j += 2
            k += 2
            s += 1
        ###########################################################################
        # Calcul 4. Total cost of sales (vehicles & parts) first row
        i = 276
        j = 131
        while(i < 281 and j < 136):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 1

        # Calcul 4. Total cost of sales (vehicles & parts) second row
        i = 281
        j = 207
        while(i < 286 and j < 217):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 2

        # Calcul 4. Total cost of sales (vehicles & parts) third row
        i = 286
        j = 267
        while(i < 291 and j < 277):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 2

         # Calcul 4. Total cost of sales (vehicles & parts) fourth row
        i = 291
        j = 267
        while(i < 296 and j < 277):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 2



         # Calcul Weighted average margin DAF parts
        #=IF($'7.2.2 Turnover Parts'.C17=0,0,((($'7.2.2 Turnover Parts'.C36-$'7.2.2 Turnover Parts'.C26)
        # *$'7.3 Cost of sales'.B76)+($'7.2.2 Turnover Parts'.C26*$'7.3 Cost of sales'.B78)
        # +($'7.2.2 Turnover Parts'.C41*$'7.3 Cost of sales'.B80))
        # /($'7.2.2 Turnover Parts'.C17+1E-016))

        #float( dict_2["TurnoverParts_Input" + str(m)])

        i = 20
        k = 36
        m = 56
        s = 76
        j = 156
        n = 176
        b = 186
        aa = 217
        total = 0
        while( aa < 226):
            parts_1 = float( dict_2["TurnoverParts_Input" + str(i)])
            parts_2 = float( dict_2["TurnoverParts_Input" + str(k)])
            parts_3 = float( dict_2["TurnoverParts_Input" + str(m)])
            parts_4 = float( dict_2["TurnoverParts_Input" + str(s)])
            cost_1 = float(x["CostOFSales_Input" + str(j)]) / 100
            cost_2 = float(x["CostOFSales_Input" + str(n)]) / 100
            cost_3 = float(x["CostOFSales_Input" + str(b)]) / 100
            if parts_1 == 0:
                total = 0
            else:
                total = (((parts_2 - parts_3) * cost_1) + (parts_3 * cost_2) + (parts_4 * cost_3)) / (parts_1 + 0.000000001)
            x["CostOFSales_Input" + str(aa)] = round(total)
            if aa == 217:
                aa += 1
            else:
                aa += 2
            i += 1
            k += 1
            m += 1
            s += 1
            j += 2
            n += 2
            b += 2
            total = 0


        ##########################################

        # Calcul total 2.1. Gross margin

        i = 157
        a = 157
        max_1 = 207
        sum = 0
        for m in range(207, 217, 2):
            while(i < max_1):
                sum = sum + float(x["CostOFSales_Input" + str(i)])
                if i == 157 or i == 159 or i == 161 or i == 163 or i == 165:
                    i += 20
                else:
                    i += 10
            x["CostOFSales_Input" + str(m)] = round(sum)
            sum = 0
            a += 2
            i = a
            max_1 += 2



        # Calcul Bonus parts

        i = 296
        j = 267
        while( i < 301 and j < 277):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 2



        # Calcul total
        #####################################

        # Calcul total 2.1. Gross margin

        i = 276
        a = 276
        max_1 = 301
        sum = 0
        for m in range(301, 306):
            while(i < max_1):
                sum = sum + float(x["CostOFSales_Input" + str(i)])
                i += 5
            x["CostOFSales_Input" + str(m)] = round(sum)
            sum = 0
            a += 1
            i = a
            max_1 += 1













        #######################################################
        current_db.costofsale.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.costofsale.find_one({"GlobalId": "global"})
    return redirect(url_for('costofsale.costofsale')) 
    return render_template("cost-of-sales.html", data=x)

####################################################################################

@costofsale_bp.route('/costofsale/delete', methods=['GET', 'POST'])
@login_required
def costofsale_delete():
    """
x    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.costofsale.delete_many({})
    return redirect(url_for('costofsale.costofsale')) 
    return render_template("cost-of-sales.html", data=x)
