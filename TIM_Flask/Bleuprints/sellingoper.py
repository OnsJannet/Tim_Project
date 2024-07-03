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

sellingoper_bp = Blueprint('sellingoper', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["sellingoper"]

@sellingoper_bp.route('/sellingoper', methods=['GET'])
@login_required
def sellingoper():

    """
    Create new collection in the database
    """
    current_db = get_current_db() 
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["SellingOperation_Header1"] = (int(ref["basic_year"])) 
    x["SellingOperation_Header2"] = (int(ref["basic_year"]) + 1 )
    x["SellingOperation_Header3"] = (int(ref["basic_year"]) + 2 )
    x["SellingOperation_Header4"] = (int(ref["basic_year"]) + 3 )
    x["SellingOperation_Header5"] = (int(ref["basic_year"]) + 4 )   

    i = 1
    lst = []
    while(i < 269):
        lst.append(("SellingOperation_Input" + str(i)))
        i += 1
    #print(lst)
    for entry in lst:
        x[entry] = 0
    #print(x)
    current_db.sellingoper.insert_one(x)
    x = current_db.sellingoper.find_one({"GlobalId": "global"})
    return render_template("selling-operations.html", data=x)

####################################################################################

@sellingoper_bp.route('/sellingoper/update', methods=['GET', 'POST'])
@login_required
def sellingoper_update():
    """
    Update a company in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["SellingOperation_Header1"] = (int(ref["basic_year"])) 
        x["SellingOperation_Header2"] = (int(ref["basic_year"]) + 1 )
        x["SellingOperation_Header3"] = (int(ref["basic_year"]) + 2 )
        x["SellingOperation_Header4"] = (int(ref["basic_year"]) + 3 )
        x["SellingOperation_Header5"] = (int(ref["basic_year"]) + 4 ) 
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'

        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        Senario = float(data["DealeArea_Input1"])

        #1.2 Operating Expenses
    # Calculation Total operating expenses

        i = 10
        k = 100
        Total = 0
        n = 10
        m = 100
        while(i < 15):
            for j in range(n, m, 5):
                Total = Total + round(float(x["SellingOperation_Input" + str(j)]), 3)
            x["SellingOperation_Input" + str(k)] = round((Total * (Senario / 100)))
            k += 1
            i += 1
            Total = 0
            n += 1
            m += 1
            j += 1

    #Calculation 2.1 Allocation of selling expenses to activities
        i = 159
        Selling_expense = 0
        while(i < 163):
            Selling_expense = round(Selling_expense + round(float(x["SellingOperation_Input" + str(i)])))
            i += 1
        if Selling_expense == 100:
            x["SellingOperation_Input163"] = "100.00"
        else:
            x["SellingOperation_Input163"] = "error"


    # Calculation Total operating expenses
    #2.2 Allocation of operating expenses to activities
        k = 168
        Total = 0
        n = 164
        m = 168
        for i in range (0, 18):
            for j in range(n, m):
                print(x["SellingOperation_Input" + str(j)])
                Total = Total + round(float(x["SellingOperation_Input" + str(j)]))
            if Total != 100:
                x["SellingOperation_Input" + str(k)] = "error"
            else:
                x["SellingOperation_Input" + str(k)] = "100.00"
            if k == 198 or k == 218 or k == 228:
                k += 10
            else:
                k += 5
            if (n == 194 or n == 214 or n == 224):
                n += 10
            else:
                n += 5
            if (m == 198 or m == 218 or m == 228):
                m += 10
            else:
                m += 5
            Total = 0
            print(m)
            
    #condition =IF(new + parts + service + admin <>100%,"error",E68+F68+G68+I68+H68+JI6868)


        ####################
        current_db.sellingoper.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.sellingoper.find_one({"GlobalId": "global"})
    return redirect(url_for('sellingoper.sellingoper')) 
    return render_template("selling-operations.html", data=x)


####################################################################################

@sellingoper_bp.route('/sellingoper/delete', methods=['GET', 'POST'])
@login_required
def sellingoper_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.sellingoper.delete_many({})
    return redirect(url_for('sellingoper.sellingoper'))    
    return render_template("turnover-parts.html", data=x)