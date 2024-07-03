import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
import math
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

turnovervehicle_bp= Blueprint('turnovervehicle', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["turnovervehicle"]

@turnovervehicle_bp.route('/turnovervehicle', methods=['GET'])
@login_required
def turnovervehicle():
    """
    Create new collection in the database
    """
    current_db = get_current_db()    
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["TurnoverVehicle_Header1"] = (int(ref["basic_year"])) 
    x["TurnoverVehicle_Header2"] = (int(ref["basic_year"]) + 1 )
    x["TurnoverVehicle_Header3"] = (int(ref["basic_year"]) + 2 )
    x["TurnoverVehicle_Header4"] = (int(ref["basic_year"]) + 3 )
    x["TurnoverVehicle_Header5"] = (int(ref["basic_year"]) + 4 ) 

    x["TurnoverVehicle_Header6"] = (int(ref["basic_year"])) 
    x["TurnoverVehicle_Header7"] = (int(ref["basic_year"]) + 1 )
    x["TurnoverVehicle_Header8"] = (int(ref["basic_year"]) + 2 )
    x["TurnoverVehicle_Header9"] = (int(ref["basic_year"]) + 3 )
    x["TurnoverVehicle_Header10"] = (int(ref["basic_year"]) + 4 ) 

    x["TurnoverVehicle_Header11"] = (int(ref["basic_year"])) 
    x["TurnoverVehicle_Header12"] = (int(ref["basic_year"]) + 1 )
    x["TurnoverVehicle_Header13"] = (int(ref["basic_year"]) + 2 )
    x["TurnoverVehicle_Header14"] = (int(ref["basic_year"]) + 3 )
    x["TurnoverVehicle_Header15"] = (int(ref["basic_year"]) + 4 ) 

    x["TurnoverVehicle_Header16"] = (int(ref["basic_year"])) 
    x["TurnoverVehicle_Header17"] = (int(ref["basic_year"]) + 1 )
    x["TurnoverVehicle_Header18"] = (int(ref["basic_year"]) + 2 )
    x["TurnoverVehicle_Header19"] = (int(ref["basic_year"]) + 3 )
    x["TurnoverVehicle_Header20"] = (int(ref["basic_year"]) + 4 )      





    # TurnoverVehicle_Input145
    i = 1
    lst = []
    while(i < 146):
        lst.append(("TurnoverVehicle_Input" + str(i)))
        i += 1
    #print(lst)
    for entry in lst:
        x[entry] = 0
    x["TurnoverVehicle_Input_A"] = 0
    x["TurnoverVehicle_Input_B"] = 0
    x["TurnoverVehicle_Input_C"] = 0
    x["TurnoverVehicle_Input_E"] = 0
    x["TurnoverVehicle_Input_F"] = 0
    current_db.turnovervehicle.insert_one(x)
    x = current_db.turnovervehicle.find_one({"GlobalId": "global"})
    return render_template("turnover-vehicles.html", data=x)
    

############################################################################################

@turnovervehicle_bp.route('/turnovervehicle/update', methods=['GET', 'POST'])
@login_required
def turnovervehicle_update():
    """
    Updates  collection in the database
    """
    current_db = get_current_db()    
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        ref = current_db.company.find_one({"GlobalId": "global"})

        x["TurnoverVehicle_Header1"] = (int(ref["basic_year"])) 
        x["TurnoverVehicle_Header2"] = (int(ref["basic_year"]) + 1 )
        x["TurnoverVehicle_Header3"] = (int(ref["basic_year"]) + 2 )
        x["TurnoverVehicle_Header4"] = (int(ref["basic_year"]) + 3 )
        x["TurnoverVehicle_Header5"] = (int(ref["basic_year"]) + 4 ) 

        x["TurnoverVehicle_Header6"] = (int(ref["basic_year"])) 
        x["TurnoverVehicle_Header7"] = (int(ref["basic_year"]) + 1 )
        x["TurnoverVehicle_Header8"] = (int(ref["basic_year"]) + 2 )
        x["TurnoverVehicle_Header9"] = (int(ref["basic_year"]) + 3 )
        x["TurnoverVehicle_Header10"] = (int(ref["basic_year"]) + 4 ) 

        x["TurnoverVehicle_Header11"] = (int(ref["basic_year"])) 
        x["TurnoverVehicle_Header12"] = (int(ref["basic_year"]) + 1 )
        x["TurnoverVehicle_Header13"] = (int(ref["basic_year"]) + 2 )
        x["TurnoverVehicle_Header14"] = (int(ref["basic_year"]) + 3 )
        x["TurnoverVehicle_Header15"] = (int(ref["basic_year"]) + 4 )  

        x["TurnoverVehicle_Header16"] = (int(ref["basic_year"])) 
        x["TurnoverVehicle_Header17"] = (int(ref["basic_year"]) + 1 )
        x["TurnoverVehicle_Header18"] = (int(ref["basic_year"]) + 2 )
        x["TurnoverVehicle_Header19"] = (int(ref["basic_year"]) + 3 )
        x["TurnoverVehicle_Header20"] = (int(ref["basic_year"]) + 4 )                        


        ### Calculaation New DAF vehicles
        ### Average turnover per vehicle excluding bodies and VAT, but including assessories

        i = 1
        j = 2
        k = 3
        m = 10
        n = 11
        while(i < m and j < n):
            a = round(float(x["TurnoverVehicle_Input" + str(i)]) * (1 + (float(x["TurnoverVehicle_Input" + str(j)]) / 100)))
            x["TurnoverVehicle_Input" + str(k)] = a
            i += 2
            j += 2
            if k == 9:
                break
            k += 2
        
        ###################################

        i = 10
        j = 11
        k = 12
        m = 19
        n = 20
        while(i < m and j < n):
            a = round(float(x["TurnoverVehicle_Input" + str(i)]) * (1 + (float(x["TurnoverVehicle_Input" + str(j)]) / 100)))
            x["TurnoverVehicle_Input" + str(k)] = a
            i += 2
            j += 2
            if k == 18:
                break
            k += 2
        
        ##############################################
        i = 19
        j = 20
        k = 21
        m = 28
        n = 29
        while(i < m and j < n):
            a = round(float(x["TurnoverVehicle_Input" + str(i)]) * (1 + (float(x["TurnoverVehicle_Input" + str(j)]) / 100)))
            x["TurnoverVehicle_Input" + str(k)] = a
            i += 2
            j += 2
            if k == 27:
                break
            k += 2

        ###################################
        i = 28
        j = 29
        k = 30
        m = 37
        n = 38 ## change
        while(i < m and j < n):
            print("hello")
            print(float(x["TurnoverVehicle_Input" + str(j)]))
            a = round(float(x["TurnoverVehicle_Input" + str(i)]) * (1 + (float(x["TurnoverVehicle_Input" + str(j)]) / 100)))
            x["TurnoverVehicle_Input" + str(k)] = a
            i += 2
            j += 2
            if k == 36:
                break
            k += 2
        
        ###################################
        i = 37
        j = 38
        k = 39
        m = 46
        n = 47
        while(i < m and j < n):
            a = round(float(x["TurnoverVehicle_Input" + str(i)]) * (1 + (float(x["TurnoverVehicle_Input" + str(j)]) / 100)))
            x["TurnoverVehicle_Input" + str(k)] = a
            i += 2
            j += 2
            if k == 45:
                break
            k += 2

        ###################################
        i = 46
        j = 47
        k = 48
        while(i < 54 and j < 55 and k < 56):
            a = round(float(x["TurnoverVehicle_Input" + str(i)]) * (1 + (float(x["TurnoverVehicle_Input" + str(j)]) / 100)),3)
            x["TurnoverVehicle_Input" + str(k)] = round(a) 
            i += 2
            print(i)
            j += 2
            k += 2

        ##############################################################################################
        #### CalculationAverage turnover fleet sales per vehicle excluding bodies and VAT, but including assessories
        ### Price correction fleet sales % (input)
        Price_correction = round(float(x["TurnoverVehicle_Input55"]), 1) / 100
        i = 1
        m = 56
        j = 56
        s = 86
        while(j < s and i < m):
            a = round((float(x["TurnoverVehicle_Input" + str(i)])) * (1 - Price_correction))
            x["TurnoverVehicle_Input" + str(j)] = round(a)
            print(x["TurnoverVehicle_Input" + str(j)])
            i += 9
            j += 5

        ### Price correction fleet sales % (input)
        i = 3
        m = 57
        j = 57
        s = 87
        while(j < s and i < m):
            a = round((float(x["TurnoverVehicle_Input" + str(i)])) * (1 - Price_correction))
            x["TurnoverVehicle_Input" + str(j)] = round(a)
            i += 9
            j += 5


        ### Price correction fleet sales % (input)
        i = 5
        m = 58
        j = 58
        s = 88
        while(j < s and i < m):
            a = round((float(x["TurnoverVehicle_Input" + str(i)])) * (1 - Price_correction))
            x["TurnoverVehicle_Input" + str(j)] = round(a)
            i += 9
            j += 5

        ### Price correction fleet sales % (input)
        i = 7
        m = 59
        j = 59
        s = 89
        while(j < s and i < m):
            a = round((float(x["TurnoverVehicle_Input" + str(i)])) * (1 - Price_correction),3)
            x["TurnoverVehicle_Input" + str(j)] = round(a,3)
            i += 9
            j += 5

        ### Price correction fleet sales % (input)
        i = 9
        m = 60
        j = 60          #TurnoverVehicle_Input54
        s = 90
        while(j < s and i < m):
            a = round((float(x["TurnoverVehicle_Input" + str(i)])) * (1 - Price_correction),3)
            x["TurnoverVehicle_Input" + str(j)] = round(a,3)
            i += 9
            j += 5

        ###########################################################
        #Calculation Decision number of salesmen:
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        Senario = float(data["DealeArea_Input1"])
        k = 42
        s = 47
        i = 116
        j = 121
        n = 126
        while(i < j and j < n and k < s):
            result = (Senario * data["DealeArea_Input" + str(k)]) / 100
            num_1 = float(x["TurnoverVehicle_Input" + str(i)])
            if num_1 == 0:
                x["TurnoverVehicle_Input" + str(j)] = 0
            else:
                result_2 = result / float(num_1)
                x["TurnoverVehicle_Input" + str(j)] = round(result_2)
            i += 1
            j += 1
            k += 1

        #IF($'7.2.1 Turnover Vehicles'.C82=0,0,$'7.1 Dealer area'.C35/$'7.2.1 Turnover Vehicles'.C82)

         # Calculation Total turnover DAF vehicles
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        p = 48
        q = 123
        k = 133
        s = 193
        i = 1
        n = 55
        j = 56
        m = 86
        r = 86
        r_1 = 116
        sum = 0
        while(p < q and k < s and i < n and j < m and r < r_1):
            num_1 = float(data["DealeArea_Input" + str(p)]) # C39
            num_2 = float(data["DealeArea_Input" + str(k)]) # C50
            num_3 = float(x["TurnoverVehicle_Input" + str(i)]) #C10
            num_4 = float(x["TurnoverVehicle_Input" + str(j)]) #C20
            result = math.trunc((num_1 - num_2) * num_3) + (num_2 * num_4)
            x["TurnoverVehicle_Input" + str(r)] = result
            i += 9
            j += 5
            r += 5
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + result
        x["TurnoverVehicle_Input_A"] = round(sum + 4)

        # Calculation Total turnover DAF vehicles
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        p = 50
        q = 125
        k = 135
        s = 195
        i = 3
        n = 57
        j = 57
        m = 87
        r = 87
        r_1 = 117
        sum = 0
        while(p < q and k < s and i < n and j < m and r < r_1):
            num_1 = float(data["DealeArea_Input" + str(p)]) # C39
            num_2 = float(data["DealeArea_Input" + str(k)]) # C50
            num_3 = float(x["TurnoverVehicle_Input" + str(i)]) #C10
            num_4 = float(x["TurnoverVehicle_Input" + str(j)]) #C20
            result = math.trunc((num_1 - num_2) * num_3) + (num_2 * num_4)
            x["TurnoverVehicle_Input" + str(r)] = result
            i += 9
            j += 5
            r += 5
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + result
        x["TurnoverVehicle_Input_B"] = round(sum + 11)
        
        # Calculation Total turnover DAF vehicles
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        p = 52
        q = 127
        k = 137
        s = 197
        i = 5
        n = 59
        j = 58
        m = 88
        r = 88
        r_1 = 118
        sum = 0
        while(p < q and k < s and i < n and j < m and r < r_1):
            num_1 = float(data["DealeArea_Input" + str(p)]) # C39
            num_2 = float(data["DealeArea_Input" + str(k)]) # C50
            num_3 = float(x["TurnoverVehicle_Input" + str(i)]) #C10
            num_4 = float(x["TurnoverVehicle_Input" + str(j)]) #C20
            result = math.trunc((num_1 - num_2) * num_3) + (num_2 * num_4)
            x["TurnoverVehicle_Input" + str(r)] = result
            i += 9
            j += 5
            r += 5
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + result
        x["TurnoverVehicle_Input_C"] = round(sum + 19)


        # Calculation Total turnover DAF vehicles
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        p = 54
        q = 129
        k = 139
        s = 199
        i = 7
        n = 61
        j = 59
        m = 89
        r = 89
        r_1 = 119
        sum = 0
        while(p < q and k < s and i < n and j < m and r < r_1):
            num_1 = float(data["DealeArea_Input" + str(p)]) # C39
            num_2 = float(data["DealeArea_Input" + str(k)]) # C50
            num_3 = float(x["TurnoverVehicle_Input" + str(i)]) #C10
            num_4 = float(x["TurnoverVehicle_Input" + str(j)]) #C20
            result = math.trunc((num_1 - num_2) * num_3) + (num_2 * num_4)
            x["TurnoverVehicle_Input" + str(r)] = result
            i += 9
            j += 5
            r += 5
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + result
        x["TurnoverVehicle_Input_E"] = round(sum)

        # Calculation Total turnover DAF vehicles
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        p = 56
        q = 131
        k = 141
        s = 301
        i = 9
        n = 63
        j = 60
        m = 90
        r = 90
        r_1 = 119
        sum = 0
        while(p < q and k < s and i < n and j < m and r < r_1):
            num_1 = float(data["DealeArea_Input" + str(p)]) # C39
            num_2 = float(data["DealeArea_Input" + str(k)]) # C50
            num_3 = float(x["TurnoverVehicle_Input" + str(i)]) #C10
            num_4 = float(x["TurnoverVehicle_Input" + str(j)]) #C20
            result = math.trunc((num_1 - num_2) * num_3) + (num_2 * num_4)
            x["TurnoverVehicle_Input" + str(r)] = result
            i += 9
            j += 5
            r += 5
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + result
        x["TurnoverVehicle_Input_F"] = round(sum)
        #IF($'7.2.1 Turnover Vehicles'.C82=0,0,$'7.1 Dealer area'.C35/$'7.2.1 Turnover Vehicles'.C82)
        # Calculation totaaaaaaal
        total = 0
        m = 126
        n = 141
        for i in range(141, 146):
            for j in range(m, n, 5):
                total = total + float(x["TurnoverVehicle_Input" + str(j)])
            x["TurnoverVehicle_Input" + str(i)] = total
            m += 1
            n += 1
            total = 0
            

        #################################################
        current_db.turnovervehicle.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        
    return redirect(url_for('turnovervehicle.turnovervehicle'))         
    return render_template("turnover-vehicles.html", data=x)

@turnovervehicle_bp.route('/turnovervehicle/delete', methods=['POST'])
@login_required
def turnovervehicle_delete():
    """
    deletes the collection in the database
    """
    current_db = get_current_db()    
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x ['GlobalId'] = 'global'

        x = current_db.turnovervehicle.delete_many({})
    return redirect(url_for('turnovervehicle.turnovervehicle'))              
    return render_template("turnover-vehicles.html", data=x)