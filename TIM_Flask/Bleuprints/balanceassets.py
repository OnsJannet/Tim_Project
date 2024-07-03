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

balanceassets_bp = Blueprint('balanceassets', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["balanceassets"]

@balanceassets_bp.route('/balanceassets', methods=['GET', 'POST'])
@login_required
def balanceassets():
    """
    Create new collection in the database
    """  
    current_db = get_current_db()          
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["BalanceAssets_Header1"] = (int(ref["basic_year"])) 
    x["BalanceAssets_Header2"] = (int(ref["basic_year"]) + 1 )
    x["BalanceAssets_Header3"] = (int(ref["basic_year"]) + 2 )
    x["BalanceAssets_Header4"] = (int(ref["basic_year"]) + 3 )
    x["BalanceAssets_Header5"] = (int(ref["basic_year"]) + 4 )  
    i = 1
    lst = []
    while(i < 406):
        lst.append(("BalanceAssetsInput" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x) 


    current_db.balanceassets.insert_one(x)
    x = current_db.balanceassets.find_one({"GlobalId": "global"})
    return render_template("balance-assets.html", data=x)                          


####################################################################################

@balanceassets_bp.route('/balanceassets/update', methods=['GET', 'POST'])
@login_required
def balanceassets_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()        
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        ## database needed
        inv_depr = current_db.invdepr.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["BalanceAssets_Header1"] = (int(ref["basic_year"])) 
        x["BalanceAssets_Header2"] = (int(ref["basic_year"]) + 1 )
        x["BalanceAssets_Header3"] = (int(ref["basic_year"]) + 2 )
        x["BalanceAssets_Header4"] = (int(ref["basic_year"]) + 3 )
        x["BalanceAssets_Header5"] = (int(ref["basic_year"]) + 4 )

        x["BalanceAssetsInput1"] = round(float(inv_depr["InvDep_Input157"]))
        # =B9+$'7.4.3 Inv. & Depr.'.C11+$'7.4.3 Inv. & Depr.'.D11+$'7.4.3 Inv. & Depr.'.D54-$'7.4.3 Inv. & Depr.'.D105
        #=C9+$'7.4.3 Inv. & Depr.'.F11+$'7.4.3 Inv. & Depr.'.F54-$'7.4.3 Inv. & Depr.'.F105

        x["BalanceAssetsInput2"] = round(float(x["BalanceAssetsInput1"]) +  float(inv_depr['InvDep_Input158']) - float(inv_depr['InvDep_Input230']))
        j = 159
        m = 231
        result = 0
        for i in range(3, 7):
            result = round(float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) -  float(inv_depr['InvDep_Input' + str(m)]))
        
            x["BalanceAssetsInput" + str(i)] = result
            j += 1
            m += 1
            result = 0

        #########################################

        k = 163
        for i in range(13, 49, 6):
            x["BalanceAssetsInput" + str(i)] = round(float(inv_depr['InvDep_Input' + str(k)]))
            k += 6
        
        ########################################
        j = 164
        m = 236
        result = 0
        for i in range(14, 50, 6):
            result = round(float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) - float(inv_depr['InvDep_Input' + str(m)]))
            
            x["BalanceAssetsInput" + str(i)] = result
            if i == 32:
                m += 12
                j += 12
            else:
                m += 6
                j += 6
            result = 0
        ###########################################

        j = 165
        m = 237
        result = 0
        for i in range(15, 51, 6):
            result = float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) - float(inv_depr['InvDep_Input' + str(m)])
            
            x["BalanceAssetsInput" + str(i)] = round(result)

            if i == 33:
                m += 12
                j += 12
            else:
                m += 6
                j += 6
            result = 0
        
        ######################################

        j = 166
        m = 238
        result = 0
        for i in range(16, 52, 6):
            result = float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) -  float(inv_depr['InvDep_Input' + str(m)])
            
            x["BalanceAssetsInput" + str(i)] = round(result)
            if i == 34:
                m += 12
                j += 12
            else:
                m += 6
                j += 6
            result = 0
        ##############################
        j = 167
        m = 239
        result = 0
        for i in range(17, 53, 6):
            result = float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) -  float(inv_depr['InvDep_Input' + str(m)])
            
            x["BalanceAssetsInput" + str(i)] = round(result)

            if i == 35:
                m += 12
                j += 12
            else:
                m += 6
                j += 6
            result = 0

        ####################################
        j = 168
        m = 240
        result = 0
        for i in range(18, 54, 6):
            result = float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) -  float(inv_depr['InvDep_Input' + str(m)])
            
            x["BalanceAssetsInput" + str(i)] = round(result)
            if i == 36:
                m += 12
                j += 12
            else:
                m += 6
                j += 6
    
            result = 0

        ##########################################
        x["BalanceAssetsInput400"] = round(float(inv_depr['InvDep_Input187']))
        j = 188
        m = 260
        result = 0
        for i in range(401, 406):
            result = float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(j)]) -  float(inv_depr['InvDep_Input' + str(m)])
            
            x["BalanceAssetsInput" + str(i)] = round(result)
            j += 1
            m += 1
            result = 0









        ###########################################
        # Calcul Total

        j = 13
        a = 13
        max_1 = 49
        sum = 0
        m = 400

        for i in range(49, 55):
            while(j < max_1):
                sum = sum + round(float(x["BalanceAssetsInput" + str(j)]))
                j += 6

            x["BalanceAssetsInput" + str(i)] = round(sum) + round(float(x["BalanceAssetsInput" + str(m)]))
            a += 1
            j = a
            max_1 += 1
            m += 1
            sum = 0

    ##################################
        x["BalanceAssetsInput55"] = round(float(inv_depr["InvDep_Input211"]))


        x["BalanceAssetsInput56"] = round(float(x["BalanceAssetsInput55"]) +  float(inv_depr['InvDep_Input212']) +  float(inv_depr['InvDep_Input61']) + float(inv_depr['InvDep_Input62']) - float(inv_depr['InvDep_Input134']) + float(inv_depr['InvDep_Input285']))
        
    #############################################

        j = 213
        k = 63
        m = 135
        n = 286
        result = 0
        for i in range(57, 61):
            result = float(x["BalanceAssetsInput" + str(i - 1)]) +  float(inv_depr['InvDep_Input' + str(k)]) +  float(inv_depr['InvDep_Input' + str(j)]) -  (float(inv_depr['InvDep_Input' + str(m)]) + float(inv_depr['InvDep_Input' + str(n)]))
            
            x["BalanceAssetsInput" + str(i)] = round(result)
            j += 1
            k += 1
            m += 1
            n += 1
            result = 0



        #########################

        # Calcul Total

        a = 1
        j = 49
        k = 55
        sum = 0

        for i in range(61, 67):
            
            sum = float(x["BalanceAssetsInput" + str(a)]) + float(x["BalanceAssetsInput" + str(j)]) + float(x["BalanceAssetsInput" + str(k)])
            x["BalanceAssetsInput" + str(i)] = round(sum)

            a += 1
            j += 1
            k += 1
            sum = 0

        #################################################################################


        financial = current_db.financialrequirements.find_one({"GlobalId": "global"})
        income = current_db.financialincome.find_one({"GlobalId": "global"})
        parts = current_db.turnoverpart.find_one({"GlobalId": "global"})
        vat = current_db.vat.find_one({"GlobalId": "global"})

        ########################
        k = 92
        for i in range(68, 73):
            x["BalanceAssetsInput" + str(i)] = round(financial["FinancialRequirement_Input" + str(k)])
            k += 2

        #=IF($'7.5.2 Fin. Income & Expenses '.D18=0,0,$'7.2.2 Turnover Parts'.C71)

        if float(income['FinancialExp_Input25']) == 0:
            x["BalanceAssetsInput73"] = 0
        else:
            x["BalanceAssetsInput73"] = round(float(parts["TurnoverParts_Input153"]))


        j = 158
        k = 302
        for i in range(74, 79):
            x["BalanceAssetsInput73" + str(i)] = round(float(parts["TurnoverParts_Input" + str(j)])) - round(float(inv_depr['InvDep_Input' + str(k)]))
            i += 1
            k += 1


        ###################################################

        sum = 0
        a = 67
        j = 73
        for i in range(79, 85):
            
            sum = float(x["BalanceAssetsInput" + str(a)]) + float(x["BalanceAssetsInput" + str(j)])
            x["BalanceAssetsInput" + str(i)] = round(sum)

            a += 1
            j += 1
            sum = 0

        ####################################################

        k = 82
        for i in range(86, 91):
            x["BalanceAssetsInput" + str(i)] = round(financial["FinancialRequirement_Input" + str(k)])
            k += 2

        
        #####################################

        #=IF($'7.5.3 VAT'.C62<0,0,$'7.5.3 VAT'.C62)

        k = 120
        for i in range(92, 97):
            if vat["VAT_Input" + str(k)] < 0:
                x["BalanceAssetsInput" + str(i)] = 0
            else:
                x["BalanceAssetsInput" + str(i)] = round(vat["VAT_Input" + str(k)])
            k += 1

        ###############################################

        #=IF($'7.5.2 Fin. Income & Expenses '.D25-$'7.5.2 Fin. Income & Expenses '.D11<0,0,$'7.5.2 Fin. Income & Expenses '.D25-$'7.5.2 Fin. Income & Expenses '.D11)
        num_1 = (float(income['FinancialExp_Input73']) - float(income['FinancialExp_Input13']))
        if (num_1 < 0):
            x["BalanceAssetsInput97"] = 0
        else:
            x["BalanceAssetsInput97"] = round(float(income['FinancialExp_Input73']) - float(income['FinancialExp_Input13']))

        # =$'7.5.1 Financial Requirements'.F73+$'7.5.2 Fin. Income & Expenses '.G63+$'7.5.1 Financial Requirements'.F75

        j = 226
        k = 146
        m = 231
        sum = 0
        for i in range(98, 103):
            sum = float(financial["FinancialRequirement_Input" + str(j)]) + float(income["FinancialExp_Input" + str(k)]) + float(financial["FinancialRequirement_Input" + str(m)])
            x["BalanceAssetsInput" + str(i)] = round(sum)
            j += 1
            k += 1
            m += 1
            sum = 0
        ###################################################"
        j = 79
        a = 79
        max_1 = 103
        sum = 0

        for i in range(103, 109):
            while(j < max_1):
                sum = sum + float(x["BalanceAssetsInput" + str(j)])
                j += 6
            x["BalanceAssetsInput" + str(i)] = round(sum)
            a += 1
            j = a
            max_1 += 1
            sum = 0


        ###################################################
        j = 61
        a = 103
        sum = 0

        for i in range(109, 115):
            sum =  float(x["BalanceAssetsInput" + str(j)]) + float(x["BalanceAssetsInput" + str(a)])
            x["BalanceAssetsInput" + str(i)] = round(sum)
            a += 1
            j += 1
            sum = 0

        #########################################################################
        
        current_db.balanceassets.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.balanceassets.find_one({"GlobalId": "global"})
    return redirect(url_for('balanceassets.balanceassets'))
    return render_template("balance-assets.html", data=x)       

####################################################################################

@balanceassets_bp.route('/balanceassets/delete', methods=['GET', 'POST'])
@login_required
def balanceassets_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()        
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.balanceassets.delete_many({})
    return redirect(url_for('balanceassets.balanceassets'))
    return render_template("balance-assets.html", data=x)   