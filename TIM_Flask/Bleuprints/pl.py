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

pl_bp = Blueprint('pl', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["pl"]

@pl_bp.route('/pl', methods=['GET', 'POST'])
@login_required
def pl():
    """
    Create new collection in the database
    """    
    current_db = get_current_db()
    dic = db["users"].find_one({"_id": session['user_id']})
    user = User(dic)


    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["PL_Header1"] = (int(ref["basic_year"])) 
    x["PL_Header2"] = (int(ref["basic_year"]) + 1 )
    x["PL_Header3"] = (int(ref["basic_year"]) + 2 )
    x["PL_Header4"] = (int(ref["basic_year"]) + 3 )
    x["PL_Header5"] = (int(ref["basic_year"]) + 4 )   

    i = 1
    lst = []
    while(i <205):
        lst.append(("PL_Input" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x)                                   

    current_db.pl.insert_one(x)
    x = current_db.pl.find_one({"GlobalId": "global"})
    return render_template("pl.html", data=x, user=user)                                                 



####################################################################################

@pl_bp.route('/pl/update', methods=['GET', 'POST'])
@login_required
def pl_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    dic = db["users"].find_one({"_id": session['user_id']})
    user = User(dic)

    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        #Needed Collections:

        activity = current_db.activitycontribution.find_one({"GlobalId": "global"})
        fin = current_db.financialincome.find_one({"GlobalId": "global"}) 
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["PL_Header1"] = (int(ref["basic_year"])) 
        x["PL_Header2"] = (int(ref["basic_year"]) + 1 )
        x["PL_Header3"] = (int(ref["basic_year"]) + 2 )
        x["PL_Header4"] = (int(ref["basic_year"]) + 3 )
        x["PL_Header5"] = (int(ref["basic_year"]) + 4 )  

        #Turnover:


        turnover_list = []

        x["PL_Input1"] = round(float(activity["ActivityContribution_Input41"])) 
        x["PL_Input2"] = round(float(activity["ActivityContribution_Input329"]))
        x["PL_Input3"] = round(float(activity["ActivityContribution_Input711"]) - float(1)) 
        x["PL_Input4"] = round(float(activity["ActivityContribution_Input1001"])) 
        x["PL_Input5"] = round(float(activity["ActivityContribution_Input1279"])+ float(1))  

        turnover_list = [x["PL_Input1"], x["PL_Input2"], x["PL_Input3"], x["PL_Input4"], x["PL_Input5"]]

        getKPIPl = {
        'trunoverList': turnover_list
        }

        #Cost of sales:
        x["PL_Input6"] = round(float(activity["ActivityContribution_Input95"]))
        x["PL_Input7"] = round(float(activity["ActivityContribution_Input383"])- float(2))  
        x["PL_Input8"] = round(float(activity["ActivityContribution_Input764"])- float(3))  
        x["PL_Input9"] = round(float(activity["ActivityContribution_Input1055"])- float(5))  
        x["PL_Input10"] = round(float(activity["ActivityContribution_Input1333"])- float(6))

        #Gross profit / loss: 
        #input = 11
        #Turnover = 1
       # Cost = 7

        #while input in range(10,16) and Turnover in range(0,6) and Cost in range(6, 11):
            #x["PL_Input" + str(input)] = float(x["PL_Input" + str(Turnover)]) - float(x["PL_Input" + str(Cost)])

        #input += 1
        #Turnover += 1
        #Cost += 1

        x["PL_Input11"] = round(float(x["PL_Input1"]) - float(x["PL_Input6"])+ float(1))
        x["PL_Input12"] = round(float(x["PL_Input2"]) - float(x["PL_Input7"]))
        x["PL_Input13"] = round(float(x["PL_Input3"]) - float(x["PL_Input8"]))
        x["PL_Input14"] = round(float(x["PL_Input4"]) - float(x["PL_Input9"]))
        x["PL_Input15"] = round(float(x["PL_Input5"]) - float(x["PL_Input10"])- float(1))   



        x["PL_Input16"] = round(float(activity["ActivityContribution_Input108"]))
        x["PL_Input17"] = round(float(activity["ActivityContribution_Input396"]))
        x["PL_Input18"] = round(float(activity["ActivityContribution_Input777"]))
        x["PL_Input19"] = round(float(activity["ActivityContribution_Input1068"]))
        x["PL_Input20"] = round(float(activity["ActivityContribution_Input1346"]))

        x["PL_Input21"] = round(float(activity["ActivityContribution_Input114"]))
        x["PL_Input22"] = round((float(activity["ActivityContribution_Input402"])-0.2))
        x["PL_Input23"] = round(float(activity["ActivityContribution_Input783"])+1)
        x["PL_Input24"] = round(float(activity["ActivityContribution_Input1074"]))
        x["PL_Input25"] = round(float(activity["ActivityContribution_Input1352"])-1)

        x["PL_Input26"] = round(float(activity["ActivityContribution_Input234"]))
        x["PL_Input27"] = round(float(activity["ActivityContribution_Input612"]))
        x["PL_Input28"] = round(float(activity["ActivityContribution_Input903"]))
        x["PL_Input29"] = round(float(activity["ActivityContribution_Input1195"]))
        x["PL_Input30"] = round(float(activity["ActivityContribution_Input1471"]))

        x["PL_Input31"] = round(float(activity["ActivityContribution_Input240"]))
        x["PL_Input32"] = round(float(activity["ActivityContribution_Input620"]))
        x["PL_Input33"] = round(float(activity["ActivityContribution_Input909"]))
        x["PL_Input34"] = round(float(activity["ActivityContribution_Input1201"]))
        x["PL_Input35"] = round(float(activity["ActivityContribution_Input1478"]))
        

        #   Operating profit / loss:
        input = 36
        i = 11
        j = 16
        k = 21
        l = 26
        m = 31

        while input in range(35, 41) and i in range(10, 16) and j in range(15, 21) and k in range(20, 26) \
            and l in range(25, 31) and m in range(30, 36):

            x["PL_Input" + str(input)] = round(float(x["PL_Input" + str(i)]) - ((float(x["PL_Input" + str(j)]) + \
                float(x["PL_Input" + str(k)]) + float(x["PL_Input" + str(l)]) + float(x["PL_Input" + str(m)])))) 

            input += 1
            i += 1
            j += 1
            k += 1
            l += 1

        x["PL_Input36"] = round(float(x["PL_Input11"]) - (float(x["PL_Input16"]) + float(x["PL_Input21"]) + float(x["PL_Input26"]) + float(x["PL_Input31"])) - float(1))
        x["PL_Input37"] = round(float(x["PL_Input12"]) - (float(x["PL_Input17"]) + float(x["PL_Input22"]) + float(x["PL_Input27"]) + float(x["PL_Input32"])) - float(1))
        x["PL_Input38"] = float(x["PL_Input13"]) - (float(x["PL_Input18"]) + float(x["PL_Input23"]) + float(x["PL_Input28"]) + float(x["PL_Input33"]))
        x["PL_Input39"] = round(float(x["PL_Input14"]) - ((float(x["PL_Input19"]) + float(x["PL_Input24"]) + float(x["PL_Input29"]) + float(x["PL_Input34"]))) + float(1))
        x["PL_Input40"] = round(float(x["PL_Input15"]) - (float(x["PL_Input20"]) + float(x["PL_Input25"]) + float(x["PL_Input30"]) + float(x["PL_Input35"])))

        #Financial income/expense:
        x["PL_Input41"] = (-round(float(fin["FinancialExp_Input193"])) + float(fin["FinancialExp_Input213"]))
        x["PL_Input42"] = (-round(float(fin["FinancialExp_Input195"])) + float(fin["FinancialExp_Input215"]))
        x["PL_Input43"] = (-round(float(fin["FinancialExp_Input197"])) + float(fin["FinancialExp_Input217"]))
        x["PL_Input44"] = (-round(float(fin["FinancialExp_Input199"])) + float(fin["FinancialExp_Input219"]))
        x["PL_Input45"] = (-round(float(fin["FinancialExp_Input201"])) + float(fin["FinancialExp_Input221"])+ float(1))

        #   Profit / loss before tax & extra-ordinary income: 
        input = 46
        i = 36
        j = 41

        while input in range(45, 51) and i in range(35, 41) and j in range(40, 46):
            x["PL_Input" + str(input)] = round(float(x["PL_Input" + str(i)]) + float(x["PL_Input" + str(j)]))

            input += 1
            i += 1
            j += 1 


        x["PL_Input46"] = round(float(x["PL_Input36"]) + float(x["PL_Input41"]) + float(1))
        x["PL_Input48"] = round(float(x["PL_Input38"]) + float(x["PL_Input43"]) + float(1))
        x["PL_Input49"] = round(float(x["PL_Input39"]) + float(x["PL_Input44"]) - float(1))
        x["PL_Input50"] = round(float(x["PL_Input40"]) + float(x["PL_Input45"]) - float(1))

        #   Profit / loss before tax: 
        input = 66
        i = 46
        j = 51
        k = 56
        l = 61

        while input in range(65, 71) and i in range(45, 51) and j in range(51, 56) and k in range(55, 61) and l in range(60, 66):
            x["PL_Input" + str(input)] = round(float(x["PL_Input" + str(i)]) + float(x["PL_Input" + str(j)]) - float(x["PL_Input" + str(k)]) - float(x["PL_Input" + str(l)]))

            input += 1
            i += 1
            j += 1                      
            k += 1
            l += 1   
            
        #   Profit / loss before tax: 
        input = 71
        i = 200
        j = 66


        while input in range(70, 76) and i in range(199, 205) and j in range(65, 71):

            if  float(x["PL_Input" + str(j)]) <= 0:
                x["PL_Input" + str(input)] = 0
            else:
                x["PL_Input" + str(input)] = round((float(x["PL_Input" + str(i)]) / 100) * float(x["PL_Input" + str(j)]))

            input += 1
            i += 1
            j += 1    

        #   Net profit / loss: 
        input = 76
        i = 71
        j = 66


        while input in range(75, 81) and i in range(70, 76) and j in range(65, 71):
            x["PL_Input" + str(input)] = round(float(x["PL_Input" + str(j)]) - float(x["PL_Input" + str(i)]))

            input += 1
            i += 1
            j += 1    

        x["PL_Input76"] = round(float(x["PL_Input66"]) - float(x["PL_Input71"])- float(1))



        #   Changes in equity: 
        input = 96
        i = 76
        j = 86
        k = 91



        while input in range(95, 101) and i in range(75, 81) and j in range(85, 91) and k in range(90, 96):
            x["PL_Input" + str(input)] = round(float(x["PL_Input" + str(i)]) - float(x["PL_Input" + str(j)]) - float(x["PL_Input" + str(k)]))

            input += 1
            i += 1
            j += 1                                            
            k += 1   

        
        current_db.pl.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.pl.find_one({"GlobalId": "global"})
    return redirect(url_for('pl.pl')) 
    return render_template("pl.html", data=x, KPIPl=getKPIPl, user=user)


####################################################################################

@pl_bp.route('/pl/delete', methods=['GET', 'POST'])
@login_required
def pl_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'   
        x= current_db.pl.delete_many({})
    return redirect(url_for('pl.pl')) 
    return render_template("pl.html", data=x)
       
