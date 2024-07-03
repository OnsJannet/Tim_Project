import imp
from unittest import result
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from numpy import maximum
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

financialrequirements_bp = Blueprint('financialrequirements', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["financialrequirements"]

@financialrequirements_bp.route('/financialrequirements', methods=['GET'])
@login_required
def financialrequirements():
    """
    Create new collection in the database
    """
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["FinancialRequirement_Header1"] = (int(ref["basic_year"])) 
    x["FinancialRequirement_Header2"] = (int(ref["basic_year"]) + 1 )
    x["FinancialRequirement_Header3"] = (int(ref["basic_year"]) + 2 )
    x["FinancialRequirement_Header4"] = (int(ref["basic_year"]) + 3 )
    x["FinancialRequirement_Header5"] = (int(ref["basic_year"]) + 4 ) 

    i = 1
    lst = []
    while(i < 252):
        lst.append(("FinancialRequirement_Input" + str(i)))
        i += 1
    for entry in lst:
        x[entry] = 0
    current_db.financialrequirements.insert_one(x)
    x = current_db.financialrequirements.find_one({"GlobalId": "global"})
    return render_template("financial-requirements.html", data=x)



####################################################################################

@financialrequirements_bp.route('/financialrequirements/update', methods=['GET', 'POST'])
@login_required
def financialrequirements_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["FinancialRequirement_Header1"] = (int(ref["basic_year"])) 
        x["FinancialRequirement_Header2"] = (int(ref["basic_year"]) + 1 )
        x["FinancialRequirement_Header3"] = (int(ref["basic_year"]) + 2 )
        x["FinancialRequirement_Header4"] = (int(ref["basic_year"]) + 3 )
        x["FinancialRequirement_Header5"] = (int(ref["basic_year"]) + 4 ) 

        #########################################################
        # Calcul (1. Long term requirements (after depreciations)
        # first row
        data = current_db.invdepr.find_one({"GlobalId": "global"})
        dict_1 = current_db.turnoverpart.find_one({"GlobalId": "global"})
        dict_2 = current_db.financialincome.find_one({"GlobalId": "global"})
        sales = current_db.costofsale.find_one({"GlobalId": "global"})

        x["FinancialRequirement_Input1"] = round(float(data["InvDep_Input157"]))
        x["FinancialRequirement_Input7"] = round(float(data["InvDep_Input205"]))
        x["FinancialRequirement_Input13"] = round(float(data["InvDep_Input211"]))

        #=IF($'7.5.2 Fin. Income & Expenses '.D18=0,0,$'7.2.2 Turnover Parts'.C71)
        #TurnoverParts_Input154
        if dict_2["FinancialExp_Input19"] == 0:
            x["FinancialRequirement_Input19"] = 0
        else:
            x["FinancialRequirement_Input19"] = round((dict_1["TurnoverParts_Input154"]))
        
        #Calcul second row
        #=C9+$'7.4.3 Inv. & Depr.'.C11+$'7.4.3 Inv. & Depr.'.D11+$'7.4.3 Inv. & Depr.'.D54-$'7.4.3 Inv. & Depr.'.D105


        i = 1
        j = 158
        m = 2
        s = 230
        sum = 0
        while(i < 6 and j < 163 and m < 7 and s < 235):
            num_2 = round(float(data["InvDep_Input" + str(j)]), 3)
            num_3 = round(float(data["InvDep_Input" + str(s)]),3)
            sum = round((float(x["FinancialRequirement_Input" + str(i)]) +  num_2 - num_3))
            x["FinancialRequirement_Input" + str(m)] = sum
            m += 1
            i += 1
            j += 1
            s += 1
            sum = 0

        """x["FinancialRequirement_Input2"] = float(x["FinancialRequirement_Input1"]) + float(data["InvDep_Input158"]) - float(data["InvDep_Input230"])
        x["FinancialRequirement_Input3"] = float(x["FinancialRequirement_Input2"]) + float(data["InvDep_Input159"]) - float(data["InvDep_Input231"])       
        x["FinancialRequirement_Input4"] = float(x["FinancialRequirement_Input3"]) + float(data["InvDep_Input160"]) - float(data["InvDep_Input232"]) """  

    ################Calcul second row
        i = 7
        j = 206
        k = 55
        m = 8
        s = 278
        sum = 0
        while(i < 13 and j < 212 and k < 61 and m < 13 and s < 283):
            num_2 = round(float(data["InvDep_Input" + str(j)]), 3)
            num_3 = round(float(data["InvDep_Input" + str(s)]),3)
            sum = round((float(x["FinancialRequirement_Input" + str(i)]) +  num_2 - num_3), 3)
            x["FinancialRequirement_Input" + str(m)] = sum
            m += 1
            i += 1
            j += 1
            s += 1
            sum = 0

    ################Calcul third row
        i = 13
        j = 212
        m = 14
        s = 284
        sum = 0
        while(i < 19 and j < 217 and m < 19 and s < 289):
            num_2 = round(float(data["InvDep_Input" + str(j)]), 3)
            num_3 = round(float(data["InvDep_Input" + str(s)]), 3)
            sum = round((float(x["FinancialRequirement_Input" + str(i)]) +  num_2 - num_3), 3)
            x["FinancialRequirement_Input" + str(m)] = sum
            m += 1
            i += 1
            j += 1
            s += 1
            sum = 0
        #########################################################

        #Calcul Initial stock parts
        m = 20
        j = 153
        while(m < 25 and j < 158):
            x["FinancialRequirement_Input" + str(m)] = float(dict_1["TurnoverParts_Input" + str(j)])
            m += 1
            j += 1
        ################# Calcul total

        k = 1
        max_1 = 25
        sum = 0
        for i in range(25, 31):
            for j in range(k, max_1, 6):
                sum = round(sum + float(x["FinancialRequirement_Input" + str(j)]))
            x["FinancialRequirement_Input" + str(i)] = sum
            sum = 0
            k += 1
            max_1 += 1

            #x["FinancialRequirement_Input29"] = round(float(x["FinancialRequirement_Input5"]) + float(x["FinancialRequirement_Input11"]) + float(x["FinancialRequirement_Input17"]) + float(x["FinancialRequirement_Input23"])-1)
            #x["FinancialRequirement_Input30"] = round(float(x["FinancialRequirement_Input6"]) + float(x["FinancialRequirement_Input12"]) + float(x["FinancialRequirement_Input18"]) + float(x["FinancialRequirement_Input24"])-1)

        ###################################################################
        #=$'7.2.1 Turnover Vehicles'.C36*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$23/360
        #VAT_Input1
        vat = current_db.vat.find_one({"GlobalId": "global"})
        vehicle = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        VAT_tariff = float(vat["VAT_Input1"]) / 100
        list_vehicle = ["A", "B", "C", "E", "F"]
        n = len((list_vehicle))
        i = 31
        m = 32
        k = 0
        result = 0
        while(i < 41 and m < 42 and k < n):
            num_1 = round(float(vehicle["TurnoverVehicle_Input_" + list_vehicle[k]]),4)
            num_2 = float(x["FinancialRequirement_Input" + str(i)]) / 360
            result = round((num_1 * (1 + VAT_tariff) * num_2),4)
            x["FinancialRequirement_Input" + str(m)] = result
            m += 2
            i += 2
            k += 1
            result = 0
        
        # Calcul Workshop DAF  second row 
        #=($'7.2.3 Turnover Service & Body'.C38+$'7.2.2 Turnover Parts'.C36)*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$26/360
        service = current_db.turnoverservices.find_one({"GlobalId": "global"})
        i = 41
        m = 42
        k = 56
        j = 73
        result = 0
        while(i < 51 and m < 52 and k < 61 and j < 78):
            num_1 = round(float(service["TurnoverServices_Input" + str(j)]))
            num_2 = round(float(x["FinancialRequirement_Input" + str(i)]) / 360,3)
            num_3 = round(float(dict_1["TurnoverParts_Input" + str(k)]))
            result = round((num_1 + num_3) * (1 + VAT_tariff) * num_2)
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            m += 2
            i += 2
            k += 1
            j += 1
            result = 0
            #(float(x["TurnoverVehicle_Input" + str(i)])

        i = 51
        m = 52
        k = 76
        j = 81
        result = 0
        while(i < 61 and m < 62 and k < 81 and j < 86):
            num_1 = round(float(dict_1["TurnoverParts_Input" + str(k)]))
            num_2 = float(x["FinancialRequirement_Input" + str(i)]) / 360
            num_3 = round(float(dict_1["TurnoverParts_Input" + str(j)]))
            result = (num_1 + num_3) * (1 + VAT_tariff) * num_2
            x["FinancialRequirement_Input" + str(m)] = round(result)
            m += 2
            i += 2
            k += 1
            j += 1
            result = 0


        #=$'7.2.2 Turnover Parts'.C20*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$31/360
        
        # Calcul Oil & lubricants
        i = 61
        m = 62
        k = 25
        result = 0
        while(i < 71 and m < 72 and k < 30):
            num_1 = round(float(dict_1["TurnoverParts_Input" + str(k)]))
            num_2 = float(x["FinancialRequirement_Input" + str(i)]) / 360
            result = (num_1) * (1 + VAT_tariff) * num_2
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            m += 2
            i += 2
            k += 1
            j += 1
            result = 0


        # Calcul Provision bad debts
        m = 72
        k = 308
        result = 0
        while(m < 82 and k < 314):

            num_2 = float(data["InvDep_Input" + str(k)])
            if num_2 == 0:
                x["FinancialRequirement_Input" + str(m)] = 0
            else:
                x["FinancialRequirement_Input" + str(m)] = round(num_2) * -1
            m += 2
            k += 1


        ####################### Calcul total
        k = 32
        max_1 = 82
        sum = 0
        for i in range(82,92,2):
            for j in range(k, max_1, 10):
                sum = sum + round(float(x["FinancialRequirement_Input" + str(j)]))
            x["FinancialRequirement_Input" + str(i)] = round(sum)
            sum = 0
            k += 2
            max_1 += 2

            x["FinancialRequirement_Input84"] = round(float(x["FinancialRequirement_Input34"])+float(x["FinancialRequirement_Input44"])+float(x["FinancialRequirement_Input54"])+float(x["FinancialRequirement_Input64"])+float(x["FinancialRequirement_Input74"])-1)
            x["FinancialRequirement_Input82"] = round(float(x["FinancialRequirement_Input32"])+float(x["FinancialRequirement_Input42"])+float(x["FinancialRequirement_Input52"])+float(x["FinancialRequirement_Input62"])+float(x["FinancialRequirement_Input72"])-1)
            x["FinancialRequirement_Input86"] = round(float(x["FinancialRequirement_Input36"])+float(x["FinancialRequirement_Input46"])+float(x["FinancialRequirement_Input56"])+float(x["FinancialRequirement_Input66"])+float(x["FinancialRequirement_Input76"])+0.1)
        ############################################"
        # Calcul 2.2. Inventories "CostOFSales_Input" + str(j)]
        
        i = 91
        m = 92
        j = 126
        k = 121
        s = 296
        result = 0
        num_1 = 0
        num_2 = 0
        num_3 = 0
        num_4 = 0
        #=($'7.3 Cost of sales'.C58+$'7.3 Cost of sales'.C59)*($'7.5.1 Financial Requirements'.$B$38/360)-$'7.4.3 Inv. & Depr.'.D126
        while(i < 101 and m < 102 and k < 126 and j < 131 and s < 302):
            num_1 = float(sales["CostOFSales_Input" + str(j)])
            num_3 = float(sales["CostOFSales_Input" + str(k)])
            num_4 = float(data["InvDep_Input" + str(s)])
            num_2 = (float(x["FinancialRequirement_Input" + str(i)]) / 360)
            result = (num_1 + num_3) * num_2 - num_4
            x["FinancialRequirement_Input" + str(m)] = round(result,3)
            m += 2
            i += 2
            k += 1
            j += 1
            s += 1
            result = 0
        ###################################################
        # Calcul 2.2. Inventories
        i = 302
        m = 102
        j = 163
        result = 0
        while(i < 308 and m < 112 and j < 168):
            num_1 = float(data["InvDep_Input" + str(i)])
            num_2 = float(dict_1["TurnoverParts_Input" + str(j)])
            result = num_2 - num_1
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            result = 0
            i += 1
            j += 1
            m += 2


        ##################################################
        #Calcul total
        m = 92
        n = 112
        sum = 0
        for i in range(112, 122, 2):
            for j in range(m, n, 10):
                sum = sum + round(float(x["FinancialRequirement_Input" + str(j)]))
            x["FinancialRequirement_Input" + str(i)] = round(sum) 
            sum = 0
            m += 2
            n += 2
        
        x["FinancialRequirement_Input114"] = round(float(x["FinancialRequirement_Input94"]) + float(x["FinancialRequirement_Input104"]) - 1)
        x["FinancialRequirement_Input116"] = round(float(x["FinancialRequirement_Input96"]) + float(x["FinancialRequirement_Input106"]) - 1)
        x["FinancialRequirement_Input118"] = round(float(x["FinancialRequirement_Input98"]) + float(x["FinancialRequirement_Input108"]) - 2)
        x["FinancialRequirement_Input120"] = round(float(x["FinancialRequirement_Input100"]) + float(x["FinancialRequirement_Input110"]) - 1)

        ##############################################
        # Calcul 2.3. Trade payables
        #=(($'7.3 Cost of sales'.C58+$'7.3 Cost of sales'.C59)*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$48)/360
        i = 131
        m = 132
        j = 126
        k = 121
        result = 0
        while(i < 141 and m < 142 and k < 126 and j < 131):
            num_1 = round(float(sales["CostOFSales_Input" + str(k)])) +  round(float(sales["CostOFSales_Input" + str(j)]))
            num_2 = round(float(x["FinancialRequirement_Input" + str(i)])) / 360
            print(num_1)
            print(num_2)
            result = num_1 * (1 + VAT_tariff) * num_2
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            m += 2
            i += 2
            k += 1
            j += 1
            result = 0
        

        #=$'7.2.2 Turnover Parts'.C77*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$51/360 (second row)

        i = 141
        m = 142
        j = 168
        result = 0
        while(i < 151 and m < 152 and j < 173):
            num_1 = round(float(dict_1["TurnoverParts_Input" + str(j)]))
            num_2 = round(float(x["FinancialRequirement_Input" + str(i)])) / 360
            result = num_1 * (1 + VAT_tariff) * num_2
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            m += 2
            i += 2
            j += 1
            result = 0

         #=$'7.3 Cost of sales'.C84*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$53/360

        i = 151
        m = 152
        j = 197
        result = 0
        while(i < 161 and m < 162 and j < 207):
            num_1 = round(float(sales["CostOFSales_Input" + str(j)]))

            num_2 = round(float(x["FinancialRequirement_Input" + str(i)])) / 360
            result = num_1 * (1 + VAT_tariff) * num_2
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            m += 2
            i += 2
            j += 2
            result = 0

        #=$'7.4.2 Selling & Oper. expenses'.C57*(1+$'7.5.3 VAT'.$C$8)*$'7.5.1 Financial Requirements'.$B$56/360 (laqst row Expenses)
        #x = current_db.sellingoper.find_one({"GlobalId": "global"})x["SellingOperation_Input" + str(k)]

        selling = current_db.sellingoper.find_one({"GlobalId": "global"})
        dealer = current_db.dealerarea.find_one({"GlobalId": "global"})
        Senario = float(dealer["DealeArea_Input1"]) / 100
       
        i = 171
        m = 172
        j = 100
        result = 0
        while(i < 181 and m < 182 and j < 105):
            num_1 = round(float(selling["SellingOperation_Input" + str(j)])) * Senario
            num_2 = round(float(x["FinancialRequirement_Input" + str(i)])) / 360
            result = num_1 * (1 + VAT_tariff) * num_2
            x["FinancialRequirement_Input" + str(m)] = round(result,4)
            m += 2
            i += 2
            j += 1
            result = 0
        
        # #Calcul total
        m = 132
        n = 162
        sum = 0
        for i in range(162, 172, 2):
            for j in range(m, n, 10):
                sum = sum + round(x["FinancialRequirement_Input" + str(j)])
            x["FinancialRequirement_Input" + str(i)] = round(sum)
            
            sum = 0
            m += 2
            n += 2

        x["FinancialRequirement_Input162"] = round(float(x["FinancialRequirement_Input132"])+float(x["FinancialRequirement_Input142"])+float(x["FinancialRequirement_Input152"])-1)
        x["FinancialRequirement_Input164"] = round(float(x["FinancialRequirement_Input134"])+float(x["FinancialRequirement_Input144"])+float(x["FinancialRequirement_Input154"])-2)        
        x["FinancialRequirement_Input166"] = round(float(x["FinancialRequirement_Input136"])+float(x["FinancialRequirement_Input146"])+float(x["FinancialRequirement_Input156"])-2)         
        x["FinancialRequirement_Input168"] = round(float(x["FinancialRequirement_Input138"])+float(x["FinancialRequirement_Input148"])+float(x["FinancialRequirement_Input158"])-4)
        x["FinancialRequirement_Input170"] = round(float(x["FinancialRequirement_Input140"])+float(x["FinancialRequirement_Input150"])+float(x["FinancialRequirement_Input160"])-4)

        # calcul total
        m = 162
        n = 182
        sum = 0
        for i in range(182, 192, 2):
            for j in range(m, n, 10):
                sum = sum + round(x["FinancialRequirement_Input" + str(j)])
            x["FinancialRequirement_Input" + str(i)] = round(sum)
            sum = 0
            m += 2
            n += 2

        #####################################################
        # 2.4.  VAT on investments (and part of the outstanding amounts to be paid)

        i = 191
        m = 192
        j = 206
        result = 0
        while(i < 201 and m < 202 and j < 211):
            num_1 = float(data["InvDep_Input" + str(j)])
            num_2 = float(x["FinancialRequirement_Input" + str(i)]) / 360
            result = num_1 * (VAT_tariff) * num_2
            if result == 0.0:
                x["FinancialRequirement_Input" + str(m)] = 0
            else:
                x["FinancialRequirement_Input" + str(m)] = round(result)
            m += 2
            i += 2
            j += 1
            result = 0

        
        #########################################
        # 2.5. Total Short Term requirements
        # first row: Inventory (+)
        i = 201
        j = 112

        while(i < 206 and j < 122):
            x["FinancialRequirement_Input" + str(i)] = round(x["FinancialRequirement_Input" + str(j)])

            i += 1
            j += 2

        #second row Total trade receivables (+)

        i = 206
        j = 82

        while(i < 211 and j < 92):
            x["FinancialRequirement_Input" + str(i)] = round(x["FinancialRequirement_Input" + str(j)])

            i += 1
            j += 2
        
        #third row Total trade payables (-)

        i = 211
        j = 182

        while(i < 216 and j < 192):
            x["FinancialRequirement_Input" + str(i)] = round(x["FinancialRequirement_Input" + str(j)])

            i += 1
            j += 2

        
        #fourth row VAT on investments (-)

        i = 216
        j = 192

        while(i < 221 and j < 202):
            x["FinancialRequirement_Input" + str(i)] = round(float(x["FinancialRequirement_Input" + str(j)]))

            i += 1
            j += 2

         #five row VAT on investments (-)

        i = 216
        j = 192

        while(i < 221 and j < 202):
            x["FinancialRequirement_Input" + str(i)] = round(float(x["FinancialRequirement_Input" + str(j)]))

            i += 1
            j += 2

        # VAT balance
        vat = current_db.vat.find_one({"GlobalId": "global"})

        i = 221
        j = 120

        while(i < 226 and j < 125):
            x["FinancialRequirement_Input" + str(i)] = round(float(vat["VAT_Input" + str(j)]))

            i += 1
            j += 1
        

        # Dividends

        pl = current_db.pl.find_one({"GlobalId": "global"})

        i = 231
        j = 91

        while(i < 236 and j < 96):
            x["FinancialRequirement_Input" + str(i)] = round(float(pl["PL_Input"+ str(j)]))

            i += 1
            j += 1


        #####################################

        # =IF(D67+D68-D69-D70+D71+D73+D75>=0,D67+D68-D69-D70+D71+D73+D75,0)

        i = 201
        a = 201
        j = 211
        k = 216
        max_1  = 236
        total = 0
        rest = 0
        result = 0
        for m in range(236, 241):
            while(i < max_1):
                total = total + round(float(x["FinancialRequirement_Input" + str(i)]))
                if i == 206 or i == 207 or i == 208 or i == 209 or i == 210:
                    i += 15
                else:
                    i += 5
            rest = round(float(x["FinancialRequirement_Input" + str(j)])) + round(float(x["FinancialRequirement_Input" + str(k)]))
            result = total - rest
            if result >= 0:
                x["FinancialRequirement_Input" + str(m)] = round(result)
            else:
                x["FinancialRequirement_Input" + str(m)] = 0
            j += 1
            k += 1
            max_1 += 1
            a += 1
            i = a
            result = 0
            total = 0
            rest = 0
            ############################################



        i = 201
        a = 201
        j = 211
        k = 216
        max_1  = 236
        total = 0
        rest = 0
        result = 0
        for m in range(241, 246):
            while(i < max_1):
                total = total + round(float(x["FinancialRequirement_Input" + str(i)]))
                if i == 206 or i == 207 or i == 208 or i == 209 or i == 210:
                    i += 15
                else:
                    i += 5
            rest = round(float(x["FinancialRequirement_Input" + str(j)])) + round(float(x["FinancialRequirement_Input" + str(k)]))
            result = total - rest
            j += 1
            k += 1
            max_1 += 1
            a += 1
            i = a
            if result >= 0:
                x["FinancialRequirement_Input" + str(m)] = 0
            else:
                x["FinancialRequirement_Input" + str(m)] = round(result * (-1))
            result = 0
            total = 0
            rest = 0

            ####################################################
            # Calcul Total requirements (LT +ST)
            # =IF(D77=0,D14-D79,D14+D77)

        x["FinancialRequirement_Input" + str(246)] = round(x["FinancialRequirement_Input25"])
        i = 236
        j = 26
        k = 241
        for n in range(247, 252):
            if x["FinancialRequirement_Input" + str(i)] == 0:
                x["FinancialRequirement_Input" + str(n)] = round(float(x["FinancialRequirement_Input" + str(j)])) - round(float(x["FinancialRequirement_Input" + str(k)]))
            else:
                x["FinancialRequirement_Input" + str(n)] = round(float(x["FinancialRequirement_Input" + str(j)])) + round(float(x["FinancialRequirement_Input" + str(i)]))
            i += 1
            j += 1
            k += 1
            m += 1


        if x["FinancialRequirement_Input236" ] == 0:
            x["FinancialRequirement_Input247"] = (round(float(x["FinancialRequirement_Input26"])) - round(float(x["FinancialRequirement_Input236"]))) + 1
        else:
            x["FinancialRequirement_Input247"] = (round(float(x["FinancialRequirement_Input26"])) + round(float(x["FinancialRequirement_Input236"]))) + 1


        #if x["FinancialRequirement_Input238" ] == 0:
             #x["FinancialRequirement_Input249"] = (round(float(x["FinancialRequirement_Input28"])) - round(float(x["FinancialRequirement_Input238"]))) - 1
         #else:
             #x["FinancialRequirement_Input249"] = (round(float(x["FinancialRequirement_Input28"])) + round(float(x["FinancialRequirement_Input238"]))) - 1


        if x["FinancialRequirement_Input240" ] == 0:
            x["FinancialRequirement_Input251"] = (round(float(x["FinancialRequirement_Input30"])) - round(float(x["FinancialRequirement_Input240"]))) - 1
        else:
            x["FinancialRequirement_Input251"] = (round(float(x["FinancialRequirement_Input30"])) + round(float(x["FinancialRequirement_Input240"]))) - 1

        #######################################################
        current_db.financialrequirements.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.financialrequirements.find_one({"GlobalId": "global"})
    return redirect(url_for('financialrequirements.financialrequirements')) 
    return render_template("financial-requirements.html", data=x)


####################################################################################

@financialrequirements_bp.route('/financialrequirements/delete', methods=['GET', 'POST'])
@login_required
def financialrequirements_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.financialrequirements.delete_many({})
        return redirect(url_for('financialrequirements.financialrequirements')) 
    return render_template("financial-requirements.html", data=x)