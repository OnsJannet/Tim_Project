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
    while(i < 2100):
        lst.append(("CostOFSales_Input" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    #print(x)   

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
                x["CostOFSales_Input" + str(m)] = round(result,3)
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

        # Code correction: =(1-$B40)*'7.2.1 Turnover Vehicles'!C25-('7.2.3 Turnover Service & Body'!$B$24*'7.2.3 Turnover Service & Body'!C$34)-'7.2.2 Turnover Parts'!$B$26
        result = 2 
        percentage = 1 
        k = 1 
        services = 37
        n = 36
       

       
    
    ##################################################################
    
        j = 61
        a = 61
        k = 56
        b = 56
        m = 62
        c = 62
        n = 63
        max_1 = 121
        max_2 = 122
        max_3 = 86
        result = 0
        Senario = round(float(dict_1["TurnoverServices_Input16"]) / 100)
        num_4 = round(float( dict_2["TurnoverParts_Input35"]))
        service = round(float(dict_1["TurnoverServices_Input37"]))
        for i in range(0, 5):
            while(j < max_1 and m < max_2 and k < max_3):
                num_1 = (round(float(x["CostOFSales_Input" + str(j)]))) * Senario
                num_2 = float(data["TurnoverVehicle_Input" + str(k)])
                num_3 = (service) * float(dict_1["TurnoverServices_Input" + str(n)])
                result = ((1 - (num_1 / 100)) *  num_2) - (num_3) - num_4
                x["CostOFSales_Input" + str(m)] = round(result +0.1)
                j += 10
                m += 10
                k += 5
            result = 0
            a = a + 2
            b = b + 1
            c = c + 2
            j = a
            k = b
            m = c
            n += 1
            max_1 += 2
            max_2 += 2
            max_3 += 1

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
                num_1 = round(float(dealer["DealeArea_Input" + str(i)]),1)
                num_2 = round(float(dealer["DealeArea_Input" + str(j)]),1)
                num_3 = round(float(x["CostOFSales_Input" + str(k)]),1)
                sum = sum + ((num_1 - num_2) * num_3)
                if i == 58 or i == 60 or i == 62 or i == 64 or i == 66:
                    i += 25
                else:
                    i += 10
                j += 10
                k += 10
            x["CostOFSales_Input" + str(m)] = round(sum,4)
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
            x["CostOFSales_Input" + str(m)] = sum
            

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
            x["CostOFSales_Input" + str(i)] = round(float(x["CostOFSales_Input" + str(j)]) + float(x["CostOFSales_Input" + str(k)]))
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

        x["CostOFSales_Input167"] = (round(float(dict_2["TurnoverParts_Input420"]) ,3)  - round(float(dict_2["TurnoverParts_Input410"]) ,3)) * ( 1 - (round(float(x["CostOFSales_Input166"]) ,3)/100))
        x["CostOFSales_Input169"] = (round(float(dict_2["TurnoverParts_Input421"]) ,3)  - round(float(dict_2["TurnoverParts_Input411"]) ,3))* ( 1 - (round(float(x["CostOFSales_Input168"]) ,3)/100))
        x["CostOFSales_Input171"] = (round(float(dict_2["TurnoverParts_Input422"]) ,3)  - round(float(dict_2["TurnoverParts_Input412"]) ,3))* ( 1 - (round(float(x["CostOFSales_Input170"]) ,3)/100))
        x["CostOFSales_Input173"] = (round(float(dict_2["TurnoverParts_Input423"]) ,3)  - round(float(dict_2["TurnoverParts_Input413"]) ,3))* ( 1 - (round(float(x["CostOFSales_Input172"]) ,3)/100))
        x["CostOFSales_Input175"] = (round(float(dict_2["TurnoverParts_Input424"]) ,3)  - round(float(dict_2["TurnoverParts_Input414"]) ,3))* ( 1 - (round(float(x["CostOFSales_Input174"]) ,3)/100))     
        



        x["CostOFSales_Input177"] = round(float(dict_2["TurnoverParts_Input36"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input176"]) ,3)/100))
        x["CostOFSales_Input179"] = round(float(dict_2["TurnoverParts_Input37"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input178"]) ,3)/100))
        x["CostOFSales_Input181"] = round(float(dict_2["TurnoverParts_Input38"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input180"]) ,3)/100))
        x["CostOFSales_Input183"] = round(float(dict_2["TurnoverParts_Input39"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input182"]) ,3)/100))
        x["CostOFSales_Input185"] = round(float(dict_2["TurnoverParts_Input40"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input184"]) ,3)/100))            
        
        
        # 2.1. Marge brute (après remise accordée au client) et frais d'achat pièces (hors bonus)
        x["CostOFSales_Input187"] = round(float(dict_2["TurnoverParts_Input76"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input186"]) ,3)/100))
        x["CostOFSales_Input189"] = round(float(dict_2["TurnoverParts_Input77"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input188"]) ,3)/100))
        x["CostOFSales_Input191"] = round(float(dict_2["TurnoverParts_Input78"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input190"]) ,3)/100))
        x["CostOFSales_Input193"] = round(float(dict_2["TurnoverParts_Input79"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input192"]) ,3)/100))
        x["CostOFSales_Input195"] = round(float(dict_2["TurnoverParts_Input80"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input194"]) ,3)/100))
        
        
     
        # Calculation others row Counter DAF to spokes + Counter autres activités.
       
        
        x["CostOFSales_Input1870"] = round(float(dict_2["TurnoverParts_Input425"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1860"]) ,3)/100))
        x["CostOFSales_Input1890"] = round(float(dict_2["TurnoverParts_Input426"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1880"]) ,3)/100))
        x["CostOFSales_Input1910"] = round(float(dict_2["TurnoverParts_Input427"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1900"]) ,3)/100))
        x["CostOFSales_Input1930"] = round(float(dict_2["TurnoverParts_Input428"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1920"]) ,3)/100))
        x["CostOFSales_Input1950"] = round(float(dict_2["TurnoverParts_Input429"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1940"]) ,3)/100))
    

        x["CostOFSales_Input1970"] = round(float(dict_2["TurnoverParts_Input405"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1960"]) ,3)/100))
        x["CostOFSales_Input1990"] = round(float(dict_2["TurnoverParts_Input406"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input1980"]) ,3)/100))
        x["CostOFSales_Input2010"] = round(float(dict_2["TurnoverParts_Input407"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input2000"]) ,3)/100))
        x["CostOFSales_Input2030"] = round(float(dict_2["TurnoverParts_Input408"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input2020"]) ,3)/100))
        x["CostOFSales_Input2050"] = round(float(dict_2["TurnoverParts_Input409"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input2040"]) ,3)/100))
    



        # Calculation others Huiles & lubrifiants.
        j = 196
        k = 197
        s = 25
        max_1 = 206
        max_2 = 207
        max_3 = 30
        result = 0
        while(j < max_1):
            # =$'7.2.2 Turnover Parts'.C27*(1-$'7.3 Cost of sales'.B79)
            Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
            Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
        #Calcul
            result = round((Parts_new_trucks) * (1 - Gross_margin))
            x["CostOFSales_Input" + str(k)] = result
            j += 2
            k += 2
            s += 1
            result = 0
        

        


        

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
        ##########################################################################




        # Calcul 4. Total cost of sales (vehicles & parts) first row
        i = 276
        j = 131
        while(i < 281 and j < 136):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 1





        
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

        x["CostOFSales_Input291"] = x["CostOFSales_Input137"]
        x["CostOFSales_Input292"] = x["CostOFSales_Input139"]
        x["CostOFSales_Input293"] = x["CostOFSales_Input141"]
        x["CostOFSales_Input294"] = x["CostOFSales_Input143"]
        x["CostOFSales_Input295"] = x["CostOFSales_Input145"]




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
            cost_1 = float(x["CostOFSales_Input" + str(j)])
            cost_2 = float(x["CostOFSales_Input" + str(n)])
            cost_3 = float(x["CostOFSales_Input" + str(b)])
            if parts_1 == 0:
                total = 0
            else:
                total = (((parts_3 - parts_2) * cost_1) + (parts_2 * cost_2) + (parts_4 * cost_3)) / (parts_1 + 0.0000000000000001)
            x["CostOFSales_Input" + str(aa)] = round(total,1)
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
        j = 1870
        b = 1870
        k = 1970
        c = 1970
        max_1 = 207
        sum = 0
        res = 0
        for m in range(207, 217, 2):
            res = float(x["CostOFSales_Input" + str(j)]) + float(x["CostOFSales_Input" + str(k)])
            while(i < max_1):
                sum = sum + float(x["CostOFSales_Input" + str(i)])
                i += 10
            x["CostOFSales_Input" + str(m)] = round(sum + res)
            sum = 0
            res = 0
            a += 2
            b += 20
            c += 20
            j = b
            k = c
            i = a
            max_1 += 2



        # Calcul Bonus parts

        i = 296
        j = 237
        while( i < 301 and j < 247):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 2



        # Calcul total
        #####################################


        x["CostOFSales_Input195"] = round(float(dict_2["TurnoverParts_Input80"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input194"]) ,3)/100))
        #x["CostOFSales_Input197"] = round(float(dict_2["TurnoverParts_Input80"]) ,3)  * ( 1 - (round(float(x["CostOFSales_Input196"]) ,3)/100))


        # Calculation others Huiles & lubrifiants.
        j = 196
        k = 197
        s = 25
        max_1 = 206
        max_2 = 207
        max_3 = 30
        result = 0
        while(j < max_1):
            # =$'7.2.2 Turnover Parts'.C27*(1-$'7.3 Cost of sales'.B79)
            Parts_new_trucks = float( dict_2["TurnoverParts_Input" + str(s)])
            Gross_margin = float((x["CostOFSales_Input" + str(j)])) / 100
        #Calcul
            result = round((Parts_new_trucks) * (1 - Gross_margin))
            x["CostOFSales_Input" + str(k)] = result
            j += 2
            k += 2
            s += 1
            result = 0

        # Calcul total 2.1. Gross margin
        i = 157
        a = 157
        j = 1870
        b = 1870
        k = 1970
        c = 1970
        max_1 = 207
        sum = 0
        res = 0
        for m in range(207, 217, 2):
            res = float(x["CostOFSales_Input" + str(j)]) + float(x["CostOFSales_Input" + str(k)])
            while(i < max_1):
                sum = sum + float(x["CostOFSales_Input" + str(i)])
                i += 10
            x["CostOFSales_Input" + str(m)] = round(sum + res)
            sum = 0
            res = 0
            a += 2
            b += 20
            c += 20
            j = b
            k = c
            i = a
            max_1 += 2

        # Calcul 4. Total cost of sales (vehicles & parts) third row
        i = 281
        j = 207
        while(i < 286 and j < 217):
            x["CostOFSales_Input" + str(i)] = x["CostOFSales_Input" + str(j)]
            i += 1
            j += 2


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

        x["CostOFSales_Input301"] = round(float(x["CostOFSales_Input276"]) + float(x["CostOFSales_Input281"]) + float(x["CostOFSales_Input286"]) + float(x["CostOFSales_Input291"]) + float(x["CostOFSales_Input296"] - 1))
        x["CostOFSales_Input302"] = round(float(x["CostOFSales_Input277"]) + float(x["CostOFSales_Input282"]) + float(x["CostOFSales_Input287"]) + float(x["CostOFSales_Input292"]) + float(x["CostOFSales_Input297"] - 2))
        x["CostOFSales_Input303"] = round(float(x["CostOFSales_Input278"]) + float(x["CostOFSales_Input283"]) + float(x["CostOFSales_Input288"]) + float(x["CostOFSales_Input293"]) + float(x["CostOFSales_Input298"] - 4))
        x["CostOFSales_Input304"] = round(float(x["CostOFSales_Input279"]) + float(x["CostOFSales_Input284"]) + float(x["CostOFSales_Input289"]) + float(x["CostOFSales_Input294"]) + float(x["CostOFSales_Input299"] - 5))
        x["CostOFSales_Input305"] = round(float(x["CostOFSales_Input280"]) + float(x["CostOFSales_Input285"]) + float(x["CostOFSales_Input290"]) + float(x["CostOFSales_Input295"]) + float(x["CostOFSales_Input300"] - 6))
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
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.costofsale.delete_many({})
    return redirect(url_for('costofsale.costofsale')) 
    return render_template("cost-of-sales.html", data=x)