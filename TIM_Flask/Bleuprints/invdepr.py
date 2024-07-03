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

invdepr_bp = Blueprint('invdepr', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["invdepr"]

@invdepr_bp.route('/invdepr', methods=['GET'])
@login_required
def invdepr():
    """
    Create new collection in the database
    """
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["InvDep_Header1"] = (int(ref["basic_year"])) 
    x["InvDep_Header2"] = (int(ref["basic_year"]) + 1 )
    x["InvDep_Header3"] = (int(ref["basic_year"]) + 2 )
    x["InvDep_Header4"] = (int(ref["basic_year"]) + 3 )
    x["InvDep_Header5"] = (int(ref["basic_year"]) + 4 )   
    i = 1
    lst = []
    while(i < 331):
        if i == 235 or i == 277 or i == 295 or i == 301 or i == 307 or i == 313 or i == 319 or i == 325:
            pass
        else:
            lst.append(("InvDep_Input" + str(i)))
        i += 1
    #print(lst)
    x["InvDep_Input229"] = 0    
    for entry in lst:
        x[entry] = 0
    #print(x)
    current_db.invdepr.insert_one(x)
    x = current_db.invdepr.find_one({"GlobalId": "global"})
    return render_template("inv-dep.html", data=x)

####################################################################################


@invdepr_bp.route('/invdepr/update', methods=['GET', 'POST'])
@login_required
def invdepr_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        x['GlobalId'] = 'global'

        ref = current_db.company.find_one({"GlobalId": "global"})

        x["InvDep_Header1"] = (int(ref["basic_year"])) 
        x["InvDep_Header2"] = (int(ref["basic_year"]) + 1 )
        x["InvDep_Header3"] = (int(ref["basic_year"]) + 2 )
        x["InvDep_Header4"] = (int(ref["basic_year"]) + 3 )
        x["InvDep_Header5"] = (int(ref["basic_year"]) + 4 )  
        ##############################################
        # Calculation Total (1.1 Fixed asset value plus Investments and desinvestments over period)
        
        """m = 13
        n = 55
        sum = 0
        k = 55

        for i in range(13, 19):
            for j in range(m, n, 6):
                sum = sum + round(float(x['InvDep_Input' + str(j)]))
            x['InvDep_Input' + str(k)] = round(sum)
            m += 1
            n += 1
            k += 1
            sum = 0

        ##############################################
    

     ##############################################
        # Calculation Total (1.1 Fixed asset value plus Investments and desinvestments over period)
        
        m = 1
        a = 1
        n = 67
        sum = 0
        k = 67

        for i in range(1, 7):
            while(m < n):
                sum = sum + round(float(x['InvDep_Input' + str(m)]))
                if m == 1 or m == 2 or m == 3 or m == 4 or m == 5 or m == 6:
                    m += 54
                else:
                    m += 6
            x['InvDep_Input' + str(k)] = round(sum)
            a = a + 1
            m = a
            print(m)
            n += 1
            k += 1
            sum = 0

        ##############################################

         # Calculation Total (1.2 Depreciations on the fixed assets which were already on the balance sheet before the basisyear)
        
        m = 86
        n = 128
        sum = 0
        k = 128

        for i in range(0,5):
            for j in range(m, n, 6):
                sum = sum + round(float(x['InvDep_Input' + str(j)]))
            x['InvDep_Input' + str(k)] = round(sum)
            m += 1
            n += 1
            k += 1
            sum = 0



        ##############################################
     ##############################################
        #Calculation 1.2 Depreciations on the fixed assets which were already on the balance sheet before the basisyear
        
        m = 74
        a = 74
        n = 140
        sum = 0
        k = 140

        for i in range(0, 5):
            while(m < n):
                sum = sum + round(float(x['InvDep_Input' + str(m)]))
                if m == 74 or m == 75 or m == 76 or m == 77 or m == 78:
                    m += 54
                else:
                    m += 6
            x['InvDep_Input' + str(k)] = round(sum)
            a = a + 1
            m = a
            n += 1
            k += 1
            sum = 0"""

        parts = current_db.turnoverpart.find_one({"GlobalId": "global"})
        #### Parts stock, new or existing dealer

        m = 217
        j = 162

        while(m < 223 and j < 169):
            if m == 217:
                x['InvDep_Input' + str(m)] = round(float(parts["TurnoverParts_Input153"]))    
            else:
                x['InvDep_Input' + str(m)] = round(float(parts["TurnoverParts_Input" + str(j)]), 3)
            j += 1
            m += 1

        #x['InvDep_Input222'] = round((float(parts["TurnoverParts_Input167"]) + 1), 3)

        ##############################################
        #Calculation 1. Fixed asset value plus Investments and desinvestments over period

        m = 145
        n = 157
        sum = 0

        for i in range(0, 6):
            for j in range(m, n, 6):
                sum = sum + round(float(x['InvDep_Input' + str(j)]), 3)
            x['InvDep_Input' + str(n)] = round(sum, 3)
            m += 1
            n += 1
            sum = 0

    
    #Calculation Total investments

        m = 163
        n = 205
        sum = 0

        for i in range(0, 6):
            for j in range(m, n, 6):
                sum = sum + round(float(x['InvDep_Input' + str(j)]), 3)
            x['InvDep_Input' + str(n)] = round(sum, 3)
            m += 1
            n += 1
            sum = 0

     #########################################
        m = 158
        j = 158
        n = 223
        sum = 0

        for i in range(0, 6):
            while(j < n):
                sum = sum + round(float(x['InvDep_Input' + str(j)]), 3)
                if j == 158 or j == 159 or j == 160 or j == 161 or j == 162:
                    j += 48
                else:
                    j += 6
            x['InvDep_Input' + str(n)] = round(sum, 3)
            m += 1
            j = m
            n += 1
            sum = 0

        #changed by ons
        x['InvDep_Input223'] = float(x['InvDep_Input157']) + float(x['InvDep_Input205']) + float(x['InvDep_Input211'])+ float(x['InvDep_Input217'])
        x['InvDep_Input224'] = float(x['InvDep_Input158']) + float(x['InvDep_Input206']) + float(x['InvDep_Input212'])+ float(x['InvDep_Input218'])
        x['InvDep_Input225'] = float(x['InvDep_Input159']) + float(x['InvDep_Input207']) + float(x['InvDep_Input213'])+ float(x['InvDep_Input219'])
        x['InvDep_Input226'] = float(x['InvDep_Input160']) + float(x['InvDep_Input208']) + float(x['InvDep_Input214'])+ float(x['InvDep_Input220'])
        x['InvDep_Input227'] = float(x['InvDep_Input161']) + float(x['InvDep_Input209']) + float(x['InvDep_Input215'])+ float(x['InvDep_Input221'])
        x['InvDep_Input228'] = float(x['InvDep_Input162']) + float(x['InvDep_Input210']) + float(x['InvDep_Input216'])+ float(x['InvDep_Input222'])

        #Calculation 2. Depreciations on fixed assets =+S20/Y20 (first colone)
        # a. Intangible fixed assets Total intangible assets(1) + Total intangible assets(2)
        i = 157
        j = 158
        k = 229
        m = 230    
        while(i < 205 and j < 206 and k < 277 and m <278):
            num_s = round(float(x['InvDep_Input' + str(i)])) + round(float(x['InvDep_Input' + str(j)]),3)
            if i == 157 and j == 158:
                i += 12
                j += 12
            else:
                i += 6
                j += 6
            
            #=IF(B82=0,0,T26)
            #=ROUND(100/(B$82*100),0)
            #=ROUND(100/)
            annual_depreciation = round((float(x['InvDep_Input' + str(k)]) / 100), 3)
            
            #round((float(2. Depreciations on fixed assets a. Intangible fixed assets annual depreciation percentage / 100)))
            if annual_depreciation == 0:
                x['InvDep_Input' + str(m)] = 0
            else:
                year = round(100/(annual_depreciation * 100),0)
                if m == 242:
                   x['InvDep_Input' + str("242")] = round((num_s / 20))
                elif m == 254:
                    x['InvDep_Input' + str("254")] = round((num_s / 5 ))
                else:
                    x['InvDep_Input' + str(m)] = round((num_s / year))
            print(x['InvDep_Input' + str(m)])
            if k == 229:
                k += 12
            else:
                k += 6
            if m == 230:
                m += 12
            else:
                m += 6
            

         # Calculation 
        m = 242
        n = 278
        sum = 0

        while(m < 278):
            sum = sum + round(float(x['InvDep_Input' + str(m)]), 3)
            m += 6
        x['InvDep_Input' + str(n)] = round(sum)

         #Calculation 2. Depreciations on fixed assets =+S20/Y20 (second colonne)
        i = 159
        j = 230
        k = 229
        m = 231
        num_1 = 0
        num_2 = 0 
        while(i < 207 and j < 278 and k < 277 and m < 279):
            num_s = round(float(x['InvDep_Input' + str(i)]))
            if i == 159:
                i += 12
            else:
                i += 6
            
            #=IF(B82=0,0,T26) =IF($Y20>=2,$S20/$Y20,0)
            #=ROUND(100/(B$82*100),0)
            annual_depreciation = (float(x['InvDep_Input' + str(k)]) / 100)
            if annual_depreciation == 0:
                num_1 = 0
                num_2 = 0

            else:
                year = round(100/(annual_depreciation * 100), 0)
                if year >= 2:
                    num_1 = float(x['InvDep_Input' + str(j)])
                else:
                    num_1 = 0
                if m == 243:
                    num_2 = round((num_s / 20))
                elif m == 255:
                    num_2 = round((num_s / 5 ))
                else:
                    num_2 = round((num_s / year ))
            x['InvDep_Input' + str(m)] = round((num_1 + num_2))
            if j == 230:
                j += 12
            else:
                j += 6
            if k == 229:
                k += 12
            else:
                k += 6
            if m == 231:
                m += 12
            else:
                m += 6
            print(m)

        # Calculation 
        m = 243
        n = 279
        sum = 0

        while(m < 279):
            sum = sum + float(x['InvDep_Input' + str(m)])
            m += 6
        x['InvDep_Input' + str(n)] = sum
       

        #Calculation 2. Depreciations on fixed assets =+S20/Y20 (third colonne)
       
        annual_depreciation = float(x['InvDep_Input' + str("229")]) / 100

        if annual_depreciation == 0.0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
            year = 0
        else:
            year = round((100 / (annual_depreciation * 100)), 0)
        if year >= 4:
            num_3 = round(float(x['InvDep_Input157']) + float(x['InvDep_Input158']))
        else:
            num_3 = 0
        if year >= 3:
            num_s = float(x['InvDep_Input159'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0
        if year >= 2:
            num_a = float(x['InvDep_Input160'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("232")] = round(num_1 + num_2 + num_3)


        # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("241")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
        else:
            year = 20 #round((100 /(annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("172")]))
        
        if year >= 3:
            num_s = float(x['InvDep_Input169']) +  float(x['InvDep_Input170'])
            num_1 = round(num_s / 20)
        else:
            num_1 = 0  
        if year >= 2:
            num_a =  float(x['InvDep_Input171'])
            num_2 = round(num_a / 20)
        else:
            num_2 = 0
        x['InvDep_Input' + str("244")] = round(num_1 + num_2 + num_3)

        ###################################################
        annual_depreciation = float(x['InvDep_Input' + str("247")]) / 100
        print("247annual_depreciation", annual_depreciation)
        if annual_depreciation == 0.0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
            year = 0
        else:
            year = round((100 / (annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("178")]))
        if year >= 3:
            num_s = float(x['InvDep_Input175']) + float(x['InvDep_Input176'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0
        if year >= 2:
            num_a = float(x['InvDep_Input177'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("250")] = round(num_1 + num_2 + num_3)


        ############################################################
        # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("253")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
        else:
            year = 5
        num_3 = round(float(x['InvDep_Input' + str("184")]))
        
        if year >= 3:
            num_s = float(x['InvDep_Input181']) +  float(x['InvDep_Input182'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0  
        if year >= 2:
            num_a =  float(x['InvDep_Input183'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("256")] = round(num_1 + num_2 + num_3)


        #########################################################
        # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("259")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
        else:
            year = round((100 /(annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("190")]))
        
        if year >= 3:
            num_s = float(x['InvDep_Input187']) +  float(x['InvDep_Input188'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0  
        if year >= 2:
            num_a =  float(x['InvDep_Input189'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("262")] = round(num_1 + num_2 + num_3)


        #########################################################
        # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("265")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
        else:
            year = round((100 /(annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("196")]))
        
        if year >= 3:
            num_s = float(x['InvDep_Input193']) +  float(x['InvDep_Input194'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0  
        if year >= 2:
            num_a =  float(x['InvDep_Input195'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("268")] = round(num_1 + num_2 + num_3)

         # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("271")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_3 = 0
        else:
            year = round((100 /(annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("201")]))
        
        if year >= 2:
            num_s = float(x['InvDep_Input199']) +  float(x['InvDep_Input200'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0  
        x['InvDep_Input' + str("273")] = round(num_1  + num_3)

         #############################################
         #########################################################
        # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("265")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
        else:
            year = round((100 /(annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("196")]))
        
        if year >= 3:
            num_s = float(x['InvDep_Input193']) +  float(x['InvDep_Input194'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0  
        if year >= 2:
            num_a =  float(x['InvDep_Input195'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("268")] = round(num_1 + num_2 + num_3)

         # value alone:
        annual_depreciation = float(x['InvDep_Input' + str("271")]) / 100
        if annual_depreciation == 0:
            num_1 = 0
            num_2 = 0
            num_3 = 0
        else:
            year = round((100 /(annual_depreciation * 100)), 0)
        num_3 = round(float(x['InvDep_Input' + str("202")]))
        
        if year >= 3:
            num_s = float(x['InvDep_Input199']) +  float(x['InvDep_Input200'])
            num_1 = round(num_s / year)
        else:
            num_1 = 0  
        if year >= 2:
            num_a =  float(x['InvDep_Input201'])
            num_2 = round(num_a / year)
        else:
            num_2 = 0
        x['InvDep_Input' + str("274")] = round(num_1 + num_2 + num_3)

        ###################################################
        # Calculation 
        m = 238
        sum = 0

        while(m < 280):
            sum = sum + round(float(x['InvDep_Input' + str(m)]))
            m += 6
        x['InvDep_Input' + str("280")] = round(sum)

        #Calculation 2. Depreciations on fixed assets =+S20/Y20 (fourth colonne)
        i = 159
        a = 160
        b = 161
        j = 230
        k = 229
        m = 233
        num_1 = 0
        num_3 = 0 
        while(i < 207 and a < 220 and j < 278 and k < 277 and m < 281 and b < 209):
            num_s = round(float(x['InvDep_Input' + str(i)]))
            if i == 159:
                i += 12
            else:
                i += 6
            num_a = round(float(x['InvDep_Input' + str(a)]))
            if a == 160:
                a += 12
            else:
                a += 6
            num_b = round(float(x['InvDep_Input' + str(b)]))
            if b == 161:
                b += 12
            else:
                b += 6
            #=IF(B82=0,0,T26) =IF($Y20>=2,$S20/$Y20,0)
            #=ROUND(100/(B$82*100),0)
            annual_depreciation = (float(x['InvDep_Input' + str(k)]) / 100)
            if annual_depreciation == 0:
                num_2 = 0
                num_3 = 0
                num_4 = 0
                num_1 = 0
            else:
                if m == 245:
                    year = 20
                elif m == 257:
                    year = 5
                else:
                    year = round(100/(annual_depreciation * 100), 0)
                if year >= 4:
                    num_1 = round(float(x['InvDep_Input' + str(j)]))
                else:
                    num_1 = 0
                if year >= 3:
                    num_2 = round((num_s / year))
                else:
                    num_2 = 0
                if year >= 2:
                    num_3 = round(num_a/ year)
                else:
                    num_3 = 0
                num_4 = round(num_b / year)

            x['InvDep_Input' + str(m)] = round((num_1 + num_2 + num_3 + num_4), 3)
            if j == 230:
                j += 12
            else:
                j += 6
            if k == 229:
                k += 12
            else:
                k += 6
            if m == 233:
                m += 12
            else:
                m += 6
         # Calculation 
        m = 245
        n = 281
        sum = 0

        while(m < 281):
            sum = sum + round(float(x['InvDep_Input' + str(m)]))
            m += 6
        x['InvDep_Input' + str(n)] = round(sum)
        #################################################
        #Calculation 2. Depreciations on fixed assets =+S20/Y20 (five colonne)
        i = 159
        a = 160
        b = 161
        c = 162
        j = 230
        k = 229
        m = 234
        num_1 = 0
        num_3 = 0 
        while(i < 207 and a < 220 and j < 278 and k < 277 and m < 282 and b < 209 and c < 210):
            num_s = round(float(x['InvDep_Input' + str(i)]))
            if i == 159:
                i += 12
            else:
                i += 6
            num_a = round(float(x['InvDep_Input' + str(a)]))
            if a == 160:
                a += 12
            else:
                a += 6
            num_b = round(float(x['InvDep_Input' + str(b)]))
            if b == 161:
                b += 12
            else:
                b += 6
            num_c = round(float(x['InvDep_Input' + str(c)]))
            if c == 162:
                c += 12
            else:
                c += 6
            #=IF(B82=0,0,T26) =IF($Y20>=2,$S20/$Y20,0)
            #=ROUND(100/(B$82*100),0)
            annual_depreciation = (float(x['InvDep_Input' + str(k)]) / 100)
            
            if annual_depreciation == 0:
                num_2 = 0
                num_3 = 0
                num_4 = 0
                num_1 = 0
                num_5 = 0
            else:
                if m == 246:
                    year = 20
                elif m == 258:
                    year = 5
                else:
                    year = round(100/(annual_depreciation * 100), 0)
                if year >= 5:
                    num_1 = round(float(x['InvDep_Input' + str(j)]))
                else:
                    num_1 = 0
                if year >= 4:
                    num_2 = round(num_s / year)
                else:
                    num_2 = 0
                if year >= 3:
                    num_3 = round(num_a/ year)
                else:
                    num_3 = 0
                if year >= 2:
                    num_4 = round(num_b / year)
                else:
                    num_4 = 0
                num_5 = round(num_c / year)

            x['InvDep_Input' + str(m)] = round((num_1 + num_2 + num_3 + num_4 + num_5), 3)
            if j == 230:
                j += 12
            else:
                j += 6
            if k == 229:
                k += 12
            else:
                k += 6
            if m == 234:
                m += 12
            else:
                m += 6
         # Calculation 
        m = 246
        n = 282
        sum = 0

        while(m < 282):
            sum = sum + round(float(x['InvDep_Input' + str(m)]))
            m += 6
        x['InvDep_Input' + str(n)] = round(sum)
        
        ######################################################
        # Calculation 	3. Amortization & Provisions for risks and costs
        m = 296
        n = 314
        k = 326
        sum = 0
        for i in range(0, 5):
            for j in range(m, n, 6):
                sum = sum + round(float(x['InvDep_Input' + str(j)]))
            x['InvDep_Input' + str(n)] = round(sum)
            x['InvDep_Input' + str(k)] = round(sum)
            sum = 0
            m += 1
            n += 1
            k += 1



        #################################################
        current_db.invdepr.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.invdepr.find_one({"GlobalId": "global"})
    return redirect(url_for('invdepr.invdepr')) 
    return render_template("inv-dep.html", data=x)


####################################################################################

@invdepr_bp.route('/invdepr/delete', methods=['GET', 'POST'])
@login_required
def invdepr_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'   
        x= current_db.invdepr.delete_many({})
    return redirect(url_for('invdepr.invdepr')) 
    return render_template("inv-dep.html", data=x)