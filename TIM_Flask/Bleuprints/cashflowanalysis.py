from functools import total_ordering
import imp
from unittest import result
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

cashflowanalysis_bp = Blueprint('cashflowanalysis', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["cashflowanalysis"]


@cashflowanalysis_bp.route('/cashflowanalysis', methods=['GET'])
@login_required
def cashflowanalysis():
    """
    Create new collection in the database
    """
    current_db = get_current_db() 
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i < 131):
        lst.append(("CashFlow_input" + str(i)))
        i += 1

    for entry in lst:
        x[entry] = 0                  
             
        
    current_db.cashflowanalysis.insert_one(x)
    x = current_db.cashflowanalysis.find_one({"GlobalId": "global"})
    return render_template("cash-flow-analysis.html", data=x)

####################################################################################

@cashflowanalysis_bp.route('/cashflowanalysis/update', methods=['GET', 'POST'])
@login_required
def cashflowanalysis_update():
    """
    Update a company in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)


        #####################################
        # Calcul (collections)
        data = current_db.pl.find_one({"GlobalId": "global"})
        inv_depr = current_db.invdepr.find_one({"GlobalId": "global"})


        ###########################################

        i = 6
        j = 76
        while(i < 11 and j < 81):
            
            x["CashFlow_input" + str(i)] = round(float(data["PL_Input" + str(j)]))
            i += 1
            j += 1


        #############################
        # Calcul c. Financial fixed assets

        """fixed_assets = []
        i = 134
        j = 284
        num = 0
        while(i < 139 and j < 289):
            num = inv_depr['InvDep_Input' + str(i)] +  inv_depr['InvDep_Input' + str(j)]
            fixed_assets.append(num)
            i += 1
            j += 1"""

        ##############################
        a = 314
        b = 284
        i = 278
        j = 230
        m = 11
        result = 0
        num_1 = 0
        while(i < 283 and j < 235 and a < 320 and b < 289 and m < 16):

            num_1 = float(inv_depr['InvDep_Input' + str(a)]) + float(inv_depr['InvDep_Input' + str(b)])
            result = inv_depr['InvDep_Input' + str(i)] +  inv_depr['InvDep_Input' + str(j)] + num_1
            x["CashFlow_input" + str(m)] = round(result)
            result = 0
            num_1 = 0
            i += 1
            j += 1
            a += 1
            b += 1
            m += 1

        ###########################################
        # Calcul A. Total

        i = 6
        j = 11
        k = 16
        sum = 0
        while(i < 11 and j < 16 and k < 21):
            sum = x["CashFlow_input" + str(i)] + x["CashFlow_input" + str(j)]
            x["CashFlow_input" + str(k)] = round(sum)
            i += 1
            j += 1
            k += 1
            sum = 0


        ###############################
        # B. 1.2 Dispositions
        # 1.3 Changer le fonds de roulement (=$'7.4.3 Inv. & Depr.'.D132-$'7.4.3 Inv. & Depr.'.B132)

        i = 319
        m = 21
        result = 0
        while(i < 324 and m < 26):

            if i == 319:
                result = float(inv_depr['InvDep_Input' + str(i + 1)])
            else:
                result = float(inv_depr['InvDep_Input' + str(i + 1)]) -  float(inv_depr['InvDep_Input' + str(i)])
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            m += 1
            result = 0

        # 1.2.1 Évolution des actifs circulants
        # (Augmentation) / Diminution des comptes débiteurs

        assets = current_db.balanceassets.find_one({"GlobalId": "global"})

        i = 85
        m = 31
        result = 0
        while(i < 90 and m < 36):
    
            result = (float(assets["BalanceAssetsInput"+ str(i + 1)]) -  float(assets["BalanceAssetsInput" + str(i)])) * (-1)
            if result == -0.0:
                result = 0.0
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            m += 1
            result = 0

        #################################
        #(Augmentation)/Diminution des stocks
        i = 79
        m = 36
        result = 0
        while(i < 84 and m < 41):
    
            result = (float(assets["BalanceAssetsInput"+ str(i + 1)]) -  float(assets["BalanceAssetsInput" + str(i)])) * (-1)
            if result == -0.0:
                result = 0.0
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            m += 1
            result = 0

        ############################
        #(Augmentation)/Diminution des autres actifs courants (hors trésorerie/banques)
        i = 91
        m = 41
        result = 0
        while(i < 96 and m < 46):
    
            result = (float(assets["BalanceAssetsInput"+ str(i + 1)]) -  float(assets["BalanceAssetsInput" + str(i)])) * (-1)
            if result == -0.0:
                result = 0.0
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            m += 1
            result = 0

        # Total
        i = 31
        a = 31
        max = 46
        sum = 0
        for j in range(46, 51):
            while(i < max):
                sum = sum + round(x["CashFlow_input" + str(i)])
                i += 5
            x["CashFlow_input" + str(j)] = round(sum)
            a += 1
            i = a
            max += 1
            sum = 0

        ###########################################

        #Calcul  (1.2.2 Évolution des passifs courants)
        # Augmentation/(diminution) des comptes créditeurs

        balence = current_db.balanceliabilities.find_one({"GlobalId": "global"})
        i = 67
        m = 56
        result = 0
        while(i < 72 and m < 61):

            result = float(balence["BalanceLiabilitiesInput" + str(i + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(i)])
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            m += 1
            result = 0

        # Augmentation/(Diminution) des autres passifs courants (hors banques & financement)

        i = 73
        m = 61
        result = 0
        while(i < 78 and m < 66):

            result = float(balence["BalanceLiabilitiesInput" + str(i + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(i)])
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            m += 1
            result = 0
        # Total
        i = 56
        a = 56
        max = 66
        sum = 0
        for j in range(66, 71):
            while(i < max):
                sum = sum + x["CashFlow_input" + str(i)]
                i += 5
            x["CashFlow_input" + str(j)] = round(sum)
            a += 1
            i = a
            max += 1
            sum = 0
        # C. Variation totale du fonds de roulement

        i = 46
        a = 46
        max = 71
        sum = 0
        for j in range(71, 76):
            while(i < max):
                sum = sum + x["CashFlow_input" + str(i)]
                i += 20
            x["CashFlow_input" + str(j)] = round(sum)
            a += 1
            i = a
            max += 1
            sum = 0
        # Cash-flow opérationnel (A+B+C)
        j = 16
        a = 21
        k = 71
        sum = 0

        for i in range(76, 81):
            sum =  x["CashFlow_input" + str(j)] + x["CashFlow_input" + str(a)] + x["CashFlow_input" + str(k)]
            x["CashFlow_input" + str(i)] = round(sum)
            a += 1
            j += 1
            k += 1
            sum = 0



        ##################################################
        # 2. Cash flows from investing activities
        # =IF($'7.5.2 Fin. Income & Expenses '.D18=0,0,$'7.9.1 Balance Assets'.C9-$'7.9.1 Balance Assets'.B9+$'7.4.3 Inv. & Depr.'.D105)
        
        income = current_db.financialincome.find_one({"GlobalId": "global"})
        print( income['FinancialExp_Input25'])
        if float(income['FinancialExp_Input25']) == 0:
            x["CashFlow_input81"] = 0
        else:
            x["CashFlow_input81"] = round(assets["BalanceAssetsInput2"] - assets["BalanceAssetsInput1"] + inv_depr['InvDep_Input230'])



        ###################################################

        i = 3
        k = 2
        j = 230
        result = 0
        for m in range(82, 86):
    
            result = - inv_depr['InvDep_Input' + str(j)] + (float(assets["BalanceAssetsInput"+ str(i)]) -  float(assets["BalanceAssetsInput" + str(k)])) * (-1)
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            k += 1
            j += 1
            result = 0

            x["CashFlow_input83"] = - inv_depr['InvDep_Input232'] + (float(assets["BalanceAssetsInput4"]) -  float(assets["BalanceAssetsInput3"])) * (-1)

        ##########################################

        i = 49
        j = 278
        k = 314
        result = 0
        for m in range(86, 91):
    
            result = - inv_depr['InvDep_Input' + str(k)] + - inv_depr['InvDep_Input' + str(j)] + (float(assets["BalanceAssetsInput"+ str(i + 1)]) -  float(assets["BalanceAssetsInput" + str(i)])) * (-1)
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            j += 1
            k += 1
            result = 0

        ###########################################

        i = 55
        j = 134
        k = 284
        result = 0
        for m in range(91, 96):
    
            result = float(inv_depr['InvDep_Input' + str(k)]) + float(inv_depr['InvDep_Input' + str(j)]) + (float(assets["BalanceAssetsInput"+ str(i + 1)]) -  float(assets["BalanceAssetsInput" + str(i)])) * (-1)
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            j += 1
            k += 1
            result = 0


        ########################################
        # total D. Flux de trésorerie provenant des activités d'investissement

        i = 81
        a = 81
        max = 96
        sum = 0
        for j in range(96, 101):
            while(i < max):
                sum = sum + round(x["CashFlow_input" + str(i)])
                i += 5
            x["CashFlow_input" + str(j)] = round(sum)
            a += 1
            i = a
            max += 1
            sum = 0

        ###########################
        # =$'7.9.2 Balance Liabilities'.C9+$'7.9.2 Balance Liabilities'.C11+$'7.9.2 Balance Liabilities'.C13-$'7.9.2 Balance Liabilities'.B9
        # -$'7.9.2 Balance Liabilities'.B11-$'7.9.2 Balance Liabilities'.B13+$'7.9.2 Balance Liabilities'.C15-$'7.9.2 Balance Liabilities'.B15+$'7.9.2 Balance Liabilities'.C17-$'7.9.2 Balance Liabilities'.B17


        i = 1
        k = 7
        j = 13
        s = 19
        n = 25
        result = 0
        for m in range(101, 106):

            num_1 = float(balence["BalanceLiabilitiesInput" + str(i + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(i)])
            num_2 = float(balence["BalanceLiabilitiesInput" + str(j + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(j)])
            num_3 = float(balence["BalanceLiabilitiesInput" + str(k + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(k)])
            num_4 = float(balence["BalanceLiabilitiesInput" + str(s + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(s)])
            num_5 = float(balence["BalanceLiabilitiesInput" + str(n + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(n)])
            result = num_1 + num_2 + num_3 + num_4 + num_5
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            k += 1
            j += 1
            s += 1
            n += 1
            result = 0

        ##################################################

        i = 55
        k = 21
        result = 0
        for m in range(106, 111):

            num_1 = float(balence["BalanceLiabilitiesInput" + str(i + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(i)])
            num_2 =  x["CashFlow_input" + str(k)]
            result = num_1 - num_2
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            k += 1
            result = 0


        #########################################
        i = 79
        result = 0
        for m in range(111, 116):
            if m == 112:
                result = float(balence["BalanceLiabilitiesInput" + str(i + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(i)]) - x["CashFlow_input22"]
            else:
                result = float(balence["BalanceLiabilitiesInput" + str(i + 1)]) -  float(balence["BalanceLiabilitiesInput" + str(i)])
            
            x["CashFlow_input" + str(m)] = round(result)
            i += 1
            k += 1
            result = 0

        #########################################

        i = 101
        a = 101
        max = 116
        sum = 0
        for j in range(116, 121):
            while(i < max):
                sum = sum + round(x["CashFlow_input" + str(i)])
                i += 5
            x["CashFlow_input" + str(j)] = round(sum)
            a += 1
            i = a
            max += 1
            sum = 0

        ##################################################


        i = 76
        k = 96
        m = 116
        sum = 0
        for j in range(121, 126):
            sum = x["CashFlow_input" + str(i)] +  x["CashFlow_input" + str(k)] +  x["CashFlow_input" + str(m)]
            x["CashFlow_input" + str(j)] = round(sum)
            i += 1
            k += 1
            m += 1
            sum = 0

        ###################################################


        x["CashFlow_input126"] = float(x["CashFlow_input121"]) + float(assets["BalanceAssetsInput97"]) - float(balence["BalanceLiabilitiesInput85"])
        x["CashFlow_input127"] = float(x["CashFlow_input122"]) + float(assets["BalanceAssetsInput98"]) - float(balence["BalanceLiabilitiesInput86"])
        x["CashFlow_input128"] = float(x["CashFlow_input123"]) + float(assets["BalanceAssetsInput99"]) - float(balence["BalanceLiabilitiesInput87"])
        x["CashFlow_input129"] = float(x["CashFlow_input124"]) + float(assets["BalanceAssetsInput100"]) - float(balence["BalanceLiabilitiesInput88"])
        x["CashFlow_input130"] = float(x["CashFlow_input125"]) + float(assets["BalanceAssetsInput101"]) - float(balence["BalanceLiabilitiesInput89"])    

        #######################################
        current_db.cashflowanalysis.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.cashflowanalysis.find_one({"GlobalId": "global"})
    return redirect(url_for('cashflowanalysis.cashflowanalysis')) 
    return render_template("cash-flow-analysis.html", data=x)

####################################################################################

@cashflowanalysis_bp.route('/cashflowanalysis/delete', methods=['GET', 'POST'])
@login_required
def cashflowanalysis_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.cashflowanalysis.delete_many({})
    return redirect(url_for('cashflowanalysis.cashflowanalysis'))  
    return render_template("cash-flow-analysis.html", data=x)
