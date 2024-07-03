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

balanceliabilities_bp = Blueprint('balanceliabilities', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["balanceliabilities"]

@balanceliabilities_bp.route('/balanceliabilities', methods=['GET', 'POST'])
@login_required
def balanceliabilities():
    """
    Create new collection in the database
    """ 
    current_db = get_current_db()          
    x = {}
    x['GlobalId'] = 'global'
    ref = db.company.find_one({"GlobalId": "global"})

    x["BalanceLiabilities_Header1"] = (int(ref["basic_year"])) 
    x["BalanceLiabilities_Header2"] = (int(ref["basic_year"]) + 1 )
    x["BalanceLiabilities_Header3"] = (int(ref["basic_year"]) + 2 )
    x["BalanceLiabilities_Header4"] = (int(ref["basic_year"]) + 3 )
    x["BalanceLiabilities_Header5"] = (int(ref["basic_year"]) + 4 )

    i = 1
    lst = []
    while(i <406):
        lst.append(("BalanceLiabilitiesInput" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x)                                   

    current_db.balanceliabilities.insert_one(x)
    x = current_db.balanceliabilities.find_one({"GlobalId": "global"})
    return render_template("balance-liabilities.html", data=x)                          


####################################################################################

@balanceliabilities_bp.route('/balanceliabilities/update', methods=['GET', 'POST'])
@login_required
def balanceliabilities_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()   
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        # needed collections:
        fin = current_db.financialincome.find_one({"GlobalId": "global"})
        vat = current_db.vat.find_one({"GlobalId": "global"})
        inv = current_db.invdepr.find_one({"GlobalId": "global"})
        reqs = current_db.financialrequirements.find_one({"GlobalId": "global"})        
        ref = current_db.company.find_one({"GlobalId": "global"})
        ass = current_db.balanceassets.find_one({"GlobalId": "global"})

        x["BalanceLiabilities_Header1"] = (int(ref["basic_year"])) 
        x["BalanceLiabilities_Header1"] = (int(ref["basic_year"]) + 1 )
        x["BalanceLiabilities_Header3"] = (int(ref["basic_year"]) + 2 )
        x["BalanceLiabilities_Header4"] = (int(ref["basic_year"]) + 3 )
        x["BalanceLiabilities_Header5"] = (int(ref["basic_year"]) + 4 )

        #Share capital:
        x["BalanceLiabilitiesInput1"] = round(float(fin["FinancialExp_Input25"]))

        input = 2
        i = 26
        j = 32

        while input in range(1,7) and i in range(25,31) and j in range(31,37):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(fin["FinancialExp_Input"  + str(i)]) + float(fin["FinancialExp_Input"  + str(j)]))

            input += 1
            i += 1
            j += 1 


        #Others:
        input_1 = 8
        input_2 = 14
        input_3 = 20
        input_4 = 26
        input_5 = 32                               

        i = 38
        j = 44
        k = 62
        l = 50
        m = 56

        while input_1 in range(7,13) and input_2 in range(13,19) and input_3 in range(19,25) and input_4 in range(25,31) and input_5 in range(31,37) and i in range(37,43) and j in range(43,49) and k in range(61,67) and l in range(49,55) and m in range(55,61):

            x["BalanceLiabilitiesInput" + str(input_1)] = round(float(fin["FinancialExp_Input"  + str(i)]))
            x["BalanceLiabilitiesInput" + str(input_2)] = round(float(fin["FinancialExp_Input"  + str(j)]))
            x["BalanceLiabilitiesInput" + str(input_3)] = round(float(fin["FinancialExp_Input"  + str(k)]))
            x["BalanceLiabilitiesInput" + str(input_4)] = round(float(fin["FinancialExp_Input"  + str(l)]))
            x["BalanceLiabilitiesInput" + str(input_5)] = round(float(fin["FinancialExp_Input"  + str(m)]))

            input_1 += 1
            input_2 += 1
            input_3 += 1
            input_4 += 1
            input_5 += 1                            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1 


        # Result in Total equity:

        i = 1
        j = 2
        k = 3
        l = 4
        m = 5
        n = 6

        o = 400
        p = 401
        q = 402
        r = 403
        s = 404
        t = 405

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []        


        while i in range(0, 32) and j in range(1, 33) and k in range(2, 34) and l in range(3, 35) and m in range(4, 36) and n in range(5, 37):

            total_i.append(float(x['BalanceLiabilitiesInput' + str(i)]))
            total_j.append(float(x['BalanceLiabilitiesInput' + str(j)]))
            total_k.append(float(x['BalanceLiabilitiesInput' + str(k)]))
            total_l.append(float(x['BalanceLiabilitiesInput' + str(l)]))
            total_m.append(float(x['BalanceLiabilitiesInput' + str(m)]))            
            total_n.append(float(x['BalanceLiabilitiesInput' + str(n)])) 

            x['BalanceLiabilitiesInput' + str(o)] =  round(sum(total_i))           
            x['BalanceLiabilitiesInput' + str(p)] =  round(sum(total_j))
            x['BalanceLiabilitiesInput' + str(q)] =  round(sum(total_k)) 
            x['BalanceLiabilitiesInput' + str(r)] =  round(sum(total_l)) 
            x['BalanceLiabilitiesInput' + str(s)] =  round(sum(total_m)) 
            x['BalanceLiabilitiesInput' + str(t)] =  round(sum(total_n))                                       

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6                                   
            n += 6


        #Provisions:
        input = 38
        i = 320

        while input in range(37, 43) and i in range(319, 325):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(inv["InvDep_Input"  + str(i)]))

            input += 1
            i += 1

        #Long term loans:
        input = 43
        i = 97

        while input in range(42, 49) and i in range(96, 103):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(fin["FinancialExp_Input"  + str(i)]))

            input += 1
            i += 1    


        #Long term loans:
        input = 50
        i = 1022

        while input in range(49, 55) and i in range(1021, 1027):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(fin["FinancialExp_Input"  + str(i)]))

            input += 1
            i += 1   

        # Total long term debts:
                       
        i = 37
        j = 38
        k = 39
        l = 40
        m = 41
        n = 42

        o = 55
        p = 56
        q = 57
        r = 58
        s = 59
        t = 60

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []        


        while i in range(36, 50) and j in range(37, 51) and k in range(38, 52) and l in range(39, 53) and m in range(40, 54) and n in range(41, 55):

            total_i.append(float(x['BalanceLiabilitiesInput' + str(i)]))
            total_j.append(float(x['BalanceLiabilitiesInput' + str(j)]))
            total_k.append(float(x['BalanceLiabilitiesInput' + str(k)]))
            total_l.append(float(x['BalanceLiabilitiesInput' + str(l)]))
            total_m.append(float(x['BalanceLiabilitiesInput' + str(m)]))            
            total_n.append(float(x['BalanceLiabilitiesInput' + str(n)])) 

            x['BalanceLiabilitiesInput' + str(o)] = round(sum(total_i) )          
            x['BalanceLiabilitiesInput' + str(p)] = round(sum(total_j)) 
            x['BalanceLiabilitiesInput' + str(q)] = round(sum(total_k) ) 
            x['BalanceLiabilitiesInput' + str(r)] = round(sum(total_l)) 
            x['BalanceLiabilitiesInput' + str(s)] = round(sum(total_m)) 
            x['BalanceLiabilitiesInput' + str(t)] = round(sum(total_n) )                                      

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6                                   
            n += 6

        #Permanent funds (equity + LT debts):

        input = 61
        i = 400
        j = 55

        while input in range(60, 67) and i in range(399, 406) and j in range(54, 61):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(x["BalanceLiabilitiesInput"  + str(i)]) + float(x["BalanceLiabilitiesInput"  + str(j)]))
        
            input += 1
            i += 1
            j += 1   
        


        #Trade payables:

        x["BalanceLiabilitiesInput68"] = round(float(reqs["FinancialRequirement_Input182"]) + float(reqs["FinancialRequirement_Input192"]))
        x["BalanceLiabilitiesInput69"] = round(float(reqs["FinancialRequirement_Input184"]) + float(reqs["FinancialRequirement_Input194"]))
        x["BalanceLiabilitiesInput70"] = round(float(reqs["FinancialRequirement_Input186"]) + float(reqs["FinancialRequirement_Input196"]))
        x["BalanceLiabilitiesInput71"] = round(float(reqs["FinancialRequirement_Input188"]) + float(reqs["FinancialRequirement_Input198"]))
        x["BalanceLiabilitiesInput72"] = round(float(reqs["FinancialRequirement_Input190"]) + float(reqs["FinancialRequirement_Input200"]))


        #VAT to be paid:
        input = 74
        i = 120


        while input in range(73, 79) and i in range(119, 125):

            if float(vat["VAT_Input" + str(i)]) < 0:
                x["BalanceLiabilitiesInput" + str(input)] = round((float(vat["VAT_Input" + str(i)])) * -1,0)
            else:              
                x["BalanceLiabilitiesInput" + str(input)] = 0
        
            input += 1
            i += 1 


        #Truck inventory financing:
        input = 80
        i = 183


        while input in range(79, 86) and i in range(182, 189):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(fin["FinancialExp_Input"  + str(i)]))
        
            input += 1
            i += 2 

        x["BalanceLiabilitiesInput80"] = round(float(fin["FinancialExp_Input134"]))
        x["BalanceLiabilitiesInput81"] = round(float(fin["FinancialExp_Input135"]))
        x["BalanceLiabilitiesInput82"] = round(float(fin["FinancialExp_Input136"]))
        x["BalanceLiabilitiesInput83"] = round(float(fin["FinancialExp_Input137"]))
        x["BalanceLiabilitiesInput84"] = round(float(fin["FinancialExp_Input138"]))
        x["BalanceLiabilitiesInput85"] = round(float(fin["FinancialExp_Input139"]))

        

        #Banks:
        input = 86
        i = 140


        while input in range(85, 91) and i in range(139, 145):
            x["BalanceLiabilitiesInput" + str(input)] = round(float(fin["FinancialExp_Input"  + str(i)]))
        
            input += 1
            i += 1                                 
             

        #Total short term debts :
        i = 67
        j = 68
        k = 69
        l = 70
        m = 71
        n = 72

        o = 91
        p = 92
        q = 93
        r = 94
        s = 95
        t = 96

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []        


        while i in range(66, 86) and j in range(67, 87) and k in range(68, 88) and l in range(69, 89) and m in range(70, 90) and n in range(71, 91):

            total_i.append(float(x['BalanceLiabilitiesInput' + str(i)]))
            total_j.append(float(x['BalanceLiabilitiesInput' + str(j)]))
            total_k.append(float(x['BalanceLiabilitiesInput' + str(k)]))
            total_l.append(float(x['BalanceLiabilitiesInput' + str(l)]))
            total_m.append(float(x['BalanceLiabilitiesInput' + str(m)]))            
            total_n.append(float(x['BalanceLiabilitiesInput' + str(n)])) 

            x['BalanceLiabilitiesInput' + str(o)] = round(sum(total_i))           
            x['BalanceLiabilitiesInput' + str(p)] = round(sum(total_j))
            x['BalanceLiabilitiesInput' + str(q)] = round(sum(total_k))
            x['BalanceLiabilitiesInput' + str(r)] = round(sum(total_l))
            x['BalanceLiabilitiesInput' + str(s)] = round(sum(total_m))
            x['BalanceLiabilitiesInput' + str(t)] = round(sum(total_n))                                     

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6                                   
            n += 6

        #Total debts :
        input = 97
        i = 55
        j = 91

        while input in range(96, 103) and i in range(54, 61) and j in range(90, 97):
            x['BalanceLiabilitiesInput' + str(input)] = round(float(x['BalanceLiabilitiesInput' + str(i)]) + float(x['BalanceLiabilitiesInput' + str(j)]))

            input += 1
            i += 1
            j += 1  

        #Total liabilities :
        input = 103
        i = 61
        j = 91

        while input in range(102, 109) and i in range(60, 67) and j in range(90, 97):
            x['BalanceLiabilitiesInput' + str(input)] = round(float(x['BalanceLiabilitiesInput' + str(i)]) + float(x['BalanceLiabilitiesInput' + str(j)]))

            input += 1
            i += 1
            j += 1  

        #Equilibrium :
        input = 109
        i = 103
        j = 109

        while input in range(108, 115) and i in range(102, 109) and j in range(108, 115):
            x['BalanceLiabilitiesInput' + str(input)] = round(float(x['BalanceLiabilitiesInput' + str(i)]) - float(ass['BalanceAssetsInput' + str(j)]))

            input += 1
            i += 1
            j += 1  


        current_db.balanceliabilities.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.balanceliabilities.find_one({"GlobalId": "global"})
    return redirect(url_for('balanceliabilities.balanceliabilities'))
    return render_template("balance-liabilities.html", data=x)       

####################################################################################

@balanceliabilities_bp.route('/balanceliabilities/delete', methods=['GET', 'POST'])
@login_required
def balanceliabilities_delete():
    """
    deletes a collection in the database
    """
    x = {}
    current_db = get_current_db()
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.balanceliabilities.delete_many({})
    return redirect(url_for('balanceliabilities.balanceliabilities'))
    return render_template("balance-liabilities.html", data=x)