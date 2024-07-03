import imp
from os import symlink
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

dealerarea_bp = Blueprint('dealerarea', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["dealerarea"]

@dealerarea_bp.route('/dealerarea', methods=['GET'])
@login_required
def dealer():
    """
    Create new collection in the database
    """
    current_db = get_current_db()    
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

        #Headers for the vehicle parc

    x["DealeArea_Header1"] = (int(ref["basic_year"])) 
    x["DealeArea_Header2"] = (int(ref["basic_year"]) + 1 )
    x["DealeArea_Header3"] = (int(ref["basic_year"]) + 2 ) 
    x["DealeArea_Header4"] = (int(ref["basic_year"]) + 3 )
    x["DealeArea_Header5"] = (int(ref["basic_year"]) + 4 ) 

    i = 1
    lst = []
    while(i < 242):
        lst.append(("DealeArea_Input" + str(i)))
        i += 1
    #print(lst)
    for entry in lst:
        x[entry] = 0
    #print(x)
    current_db.dealerarea.insert_one(x)
    x = current_db.dealerarea.find_one({"GlobalId": "global"})
    return render_template("dealer-area.html", data=x)
    
####################################################################################


@dealerarea_bp.route('/dealerarea/update', methods=['GET', 'POST'])
@login_required
def dealer_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()        
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        Senario = float(x["DealeArea_Input1"])

        # Calculation Market size dealer area
        data = current_db.vehicle.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        #Headers for the vehicle parc

        x["DealeArea_Header1"] = (int(ref["basic_year"])) 
        x["DealeArea_Header2"] = (int(ref["basic_year"]) + 1 )
        x["DealeArea_Header3"] = (int(ref["basic_year"]) + 2 ) 
        x["DealeArea_Header4"] = (int(ref["basic_year"]) + 3 )
        x["DealeArea_Header5"] = (int(ref["basic_year"]) + 4 ) 



        i = 28
        j = 36
        k = 2
        m = 7
        l = 12
        while( i != 33 and j != 41 and k != 7 and m != 12 and l != 17):
            a = (float(data["VehicleParc_Input" + str(i)]) * Senario) / 100
            b = (float(data["VehicleParc_Input" + str(j)]) * Senario) / 100
            #print(a)
            x["DealeArea_Input" + str(k)] = round(a,3)
            x["DealeArea_Input" + str(m)] = round(b,3)
            x["DealeArea_Input" + str(l)] = round((b + a))
            i += 1
            j += 1
            k += 1
            m += 1
            l += 1


        
        #Calculation Market share DAF
        i = 27
        j = 2
        l = 7
        m = 12
        k = 17
        b = 22
        while( m != 17 and l != 12 and j != 7 and k != 22 and b != 27 and i != 32):
            if x["DealeArea_Input" + str(m)] == 0:
                x["DealeArea_Input" + str(i)] = 0
            else:
                result = ((float(x["DealeArea_Input" + str(j)]) * float(x["DealeArea_Input" + str(k)])) + 
                (float(x["DealeArea_Input" + str(l)]) * float(x["DealeArea_Input" + str(b)]))) / float(x["DealeArea_Input" + str(m)])
                x["DealeArea_Input" + str(i)] = round(result, 1)
            i += 1
            j += 1
            l += 1
            m += 1
            k += 1
            b += 1
        # Calculation DAF Volume
        i = 2
        j = 7
        k = 17
        m = 22
        l = 32
        n = 37
        s = 42
        while(i != 7 and j != 12 and k != 22 and m != 32 and l != 37 and n != 42  and s != 47 ):
            a = (float(x["DealeArea_Input" + str(k)]) / 100) * (Senario / 100)
            b = (float(x["DealeArea_Input" + str(m)]) / 100) * (Senario / 100)
            res_1 = round((float(x["DealeArea_Input" + str(i)]) * a), 0)
            res_2 = round((float(x["DealeArea_Input" + str(j)]) * b), 0)
            #print(a)
            x["DealeArea_Input" + str(l)] = round(res_1)
            x["DealeArea_Input" + str(n)] = round(res_2)
            x["DealeArea_Input" + str(s)] = round((res_1 + res_2))
            i += 1
            j += 1
            k += 1
            m += 1
            l += 1
            n += 1
            s += 1


        # Calculaation DAF volume mix ( 5 -16 ton)
        i = 47
        j = 57
        k = 67
        m = 77
        while( i < 57 and j < 67 and k < 77 and m < 82):
            sum = float(x["DealeArea_Input" + str(i)]) + float(x["DealeArea_Input" + str(j)])
            x["DealeArea_Input" + str(k)] = round(sum)
            if float(x["DealeArea_Input" + str(k)]) != 100:
                x["DealeArea_Input" + str(m)] = "MIX DOES NOT EQUAL 100 %"
            else:
                x["DealeArea_Input" + str(m)] = ""
            i += 2
            j += 2
            k += 2
            m += 1


        # Calculaation DAF volume mix ( > 15 ton)
        k = 122
        m = 82
        n = 122
        sum = 0
        for i in range(82, 92, 2):
            for j in range(m, n, 10):
                sum = sum + float(x["DealeArea_Input" + str(j)])
            x["DealeArea_Input" + str(k)] = round(sum)
            sum = 0
            m = m + 2
            n = n + 2
            if k < 132:
                k = k + 2
        # Calculaation DAF volume mix (6- 15 ton) for round calculation
        p = 32
        i = 47
        j = 57
        k = 48
        n = 58
        m = 68
        while( p < 37 and i < 57 and j < 67 and k < 58 and n < 68 and m < 78):
            a = float(x["DealeArea_Input" + str(p)])
            res_1 = round(((float(x["DealeArea_Input" + str(i)]) / 100) * a), 0)
            res_2 = round(((float(x["DealeArea_Input" + str(j)]) / 100) * a), 0)
            #print(a)
            x["DealeArea_Input" + str(k)] = round(res_1)
            x["DealeArea_Input" + str(n)] = round(res_2)
            x["DealeArea_Input" + str(m)] = round((res_1 + res_2))
            i += 2
            j += 2
            k += 2
            m += 2
            n += 2
            p += 1
        # Calculaation DAF volume mix (> 15 ton) for round calculation
        p = 37
        s = 82
        b = 92
        q = 102
        num = 112
        i = 83
        j = 93
        k = 103
        n = 113
        m = 123
        while( p < 42 and i < 93 and j < 103 and k < 113 and n < 123 and m < 133 and s < 92 and b < 102 and q < 112 and num < 122):
            a = float(x["DealeArea_Input" + str(p)])
            res_1 = round(((float(x["DealeArea_Input" + str(s)]) / 100)  * a), 0)
            res_2 = round(((float(x["DealeArea_Input" + str(b)]) / 100) * a), 0)
            res_3 = round(((float(x["DealeArea_Input" + str(q)]) / 100) * a), 0)
            res_4 = round(((float(x["DealeArea_Input" + str(num)]) / 100) * a), 0)
            #print(a)
            x["DealeArea_Input" + str(i)] = round(res_1)
            x["DealeArea_Input" + str(j)] = round(res_2)
            x["DealeArea_Input" + str(k)] = round(res_3)
            x["DealeArea_Input" + str(n)] = round(res_4)
            x["DealeArea_Input" + str(m)] = round((res_1 + res_2 + res_3 + res_4))
            i += 2
            j += 2
            k += 2
            m += 2
            s += 2
            q += 2
            b += 2
            num += 2
            n += 2
            p += 1

        # Calculation Fleet vs total DAF sales
        p = 48
        q = 123
        k = 132
        s = 192
        m = 133
        n = 193
        b = 193
        sum = 0
        while(m < n and k < s and p < q):

            a = float(x["DealeArea_Input" + str(p)])
            res_1 = math.trunc(((float(x["DealeArea_Input" + str(k)]) / 100) * a))
            x["DealeArea_Input" + str(m)] = res_1
            m += 10
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + res_1
        x["DealeArea_Input" + str(b)] = sum
#######################################################################

        p = 50
        q = 123
        k = 134
        s = 194
        m = 135
        n = 195
        b = 195
        sum = 0
        while(m < n and k < s and p < q):

            a = float(x["DealeArea_Input" + str(p)])
            res_1 = math.trunc(((float(x["DealeArea_Input" + str(k)]) / 100) * a))
            x["DealeArea_Input" + str(m)] = res_1
            m += 10
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + res_1
        x["DealeArea_Input" + str(b)] = sum

    ###################################################################
        p = 52
        q = 123
        k = 136
        s = 196
        m = 137
        n = 197
        b = 197
        sum = 0
        while(m < n and k < s and p < q):

            a = float(x["DealeArea_Input" + str(p)])
            res_1 = math.trunc(((float(x["DealeArea_Input" + str(k)]) / 100) * a))
            x["DealeArea_Input" + str(m)] = res_1
            m += 10
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + res_1
        x["DealeArea_Input" + str(b)] = sum
    #####################################################################
        p = 54
        q = 123
        k = 138
        s = 198
        m = 139
        n = 199
        b = 199
        sum = 0
        while(m < n and k < s and p < q):

            a = float(x["DealeArea_Input" + str(p)])
            res_1 = math.trunc(((float(x["DealeArea_Input" + str(k)]) / 100) * a))
            x["DealeArea_Input" + str(m)] = res_1
            m += 10
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + res_1
        x["DealeArea_Input" + str(b)] = sum

    #####################################################
        p = 56
        q = 123
        k = 140
        s = 200
        m = 141
        n = 201
        b = 201
        sum = 0
        while(m < n and k < s and p < q):

            a = float(x["DealeArea_Input" + str(p)])
            res_1 = math.trunc(((float(x["DealeArea_Input" + str(k)]) / 100) * a))
            x["DealeArea_Input" + str(m)] = res_1
            m += 10
            k += 10
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            sum = sum + res_1
        x["DealeArea_Input" + str(b)] = sum
    
    ###############################################################

        """# Calculation Running parc DAF (first year)
        sum = 0
        m = 49
        n = 58
        p = 48
        q = 123
        j = 202
        k = 237
        total = 0
        while(j < k and p < q):
            for i in range(m , n):
                sum = sum + float(data["VehicleParc_Input" + str(i)])
            if j != 227:
                x["DealeArea_Input" + str(j)] = sum + float(x["DealeArea_Input" + str(p)])
            else:
                x["DealeArea_Input" + str(j)] = sum + 0
                p = p - 10
            total += float(x["DealeArea_Input" + str(j)])
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            j += 5
            m += 16
            n += 16
            sum = 0
        x["DealeArea_Input" + str(k)] = round(total)

        # Calculation Running parc DAF (second year) ############################
        sum = 0
        m = 49
        n = 58
        p = 48
        q = 125
        j = 203
        k = 238
        total = 0
        while(j < k and p < q):
            for i in range(m , n):
                sum = sum + float(data["VehicleParc_Input" + str(i)])
            if j != 228:
                x["DealeArea_Input" + str(j)] = sum + float(x["DealeArea_Input" + str(p)])
            else:
                x["DealeArea_Input" + str(j)] = sum + 0
                p = p - 10
            total += float(x["DealeArea_Input" + str(j)])
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            j += 5
            m += 16
            n += 16
            sum = 0
        x["DealeArea_Input" + str(k)] = round(total)"""

        """# Calculation Running parc DAF (third year) ######################
        sum = 0
        m = 49
        n = 58
        p = 48
        q = 127
        j = 204
        k = 239
        total = 0
        while(j < k and p < q):
            for i in range(m , n):
                sum = sum + float(data["VehicleParc_Input" + str(i)])
            if j != 229:
                x["DealeArea_Input" + str(j)] = sum + float(x["DealeArea_Input" + str(p)])
            else:
                x["DealeArea_Input" + str(j)] = sum + 0
                p = p - 10
            total += float(x["DealeArea_Input" + str(j)])
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            j += 5
            m += 16
            n += 16
            sum = 0
        x["DealeArea_Input" + str(k)] = round(total)

    # Calculation Running parc DAF (fourth year) ############################""
        sum = 0
        m = 49
        n = 58
        p = 48
        q = 129
        j = 205
        k = 240
        total = 0
        while(j < k and  p < q):
            for i in range(m , n):
                sum = sum + float(data["VehicleParc_Input" + str(i)])
            if j != 230:
                x["DealeArea_Input" + str(j)] = sum + float(x["DealeArea_Input" + str(p)])
            else:
                x["DealeArea_Input" + str(j)] = sum + 0
                p = p - 10
            total += float(x["DealeArea_Input" + str(j)])
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            j += 5
            m += 16
            n += 16
            sum = 0
        x["DealeArea_Input" + str(k)] = round(total)

    # Calculation Running parc DAF (five year) #############
        sum = 0
        m = 49
        n = 58
        p = 48
        q = 131
        j = 206
        k = 241
        total = 0
        while(j < k and p < q):
            for i in range(m , n):
                sum = sum + float(data["VehicleParc_Input" + str(i)])
            if j != 231:
                x["DealeArea_Input" + str(j)] = sum + float(x["DealeArea_Input" + str(p)])
            else:
                x["DealeArea_Input" + str(j)] = sum + 0
                p = p - 10
            total += float(x["DealeArea_Input" + str(j)])
            if p == 58 or p == 60 or p == 62 or p == 64 or p == 66:
                p += 15
            p += 10
            j += 5
            m += 16
            n += 16
            sum = 0
        x["DealeArea_Input" + str(k)] = round(total)"""
    
        # other method to calculate 6. Parc de course DAF

        short = current_db.calculationshorts.find_one({"GlobalId": "global"})

        # x["CalculationShort_Input13140"]

        i = 11
        k = 202
        while(i < 88 and k < 237):
            x["DealeArea_Input" + str(k)] = round(short["CalculationShort_Input" + str(i)])
            i += 11
            k += 5

        ###############################
        i = 99
        k = 203
        while(i < 176 and k < 238):
            x["DealeArea_Input" + str(k)] = round(short["CalculationShort_Input" + str(i)])
            i += 11
            k += 5

        ################################
        i = 188
        k = 204
        while(i < 265 and k < 239):
            x["DealeArea_Input" + str(k)] = round(short["CalculationShort_Input" + str(i)])
            i += 11
            k += 5
        #################################
        i = 265
        k = 205
        while(i < 342 and k < 240):
            x["DealeArea_Input" + str(k)] = round(short["CalculationShort_Input" + str(i)])
            i += 11
            k += 5

        ###############################

        i = 842
        k = 206
        while(i < 919 and k < 241):
            x["DealeArea_Input" + str(k)] = round(short["CalculationShort_Input" + str(i)])
            i += 11
            k += 5


        x["DealeArea_Input222"] = round(short["CalculationShort_Input88"])
        x["DealeArea_Input223"] = round(short["CalculationShort_Input177"])
        x["DealeArea_Input224"] = round(short["CalculationShort_Input13140"])
        x["DealeArea_Input225"] = round(short["CalculationShort_Input3141"])
        x["DealeArea_Input226"] = round(short["CalculationShort_Input2874"])


        # Calculate total
        i = 202
        a = 202
        max_1 = 237
        sum = 0
        for m in range(237, 242):
            while( i < max_1):
                sum = sum + x["DealeArea_Input" + str(i)]
                i += 5
            x["DealeArea_Input" + str(m)] = round(sum)
            sum = 0
            a += 1
            i = a
            max_1 += 1

        




    #######################################################

        current_db.dealerarea.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.dealerarea.find_one({"GlobalId": "global"})
    print(x)
    return redirect(url_for('dealerarea.dealer'))     
    return render_template("dealer-area.html", data=x)


####################################################################################

@dealerarea_bp.route('/dealerarea/delete',  methods=['POST'])
@login_required
def dealer_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()    
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.dealerarea.delete_many({})
    return redirect(url_for('dealerarea.dealer'))        
    return render_template("dealer-area.html", data=x)