import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
from flask import jsonify
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

calculations_bp = Blueprint('calculation', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["company"]

@calculations_bp.route('/company', methods=['GET', 'POST'])
@login_required
def company():
    """
    Create a company in the database
    """
    current_db = get_current_db()  
    print("current_db soumettre", current_db)
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        print(x)
        x['GlobalId'] = 'global'                                                                                                                                                                                                                                                                                     
        x["basic_year"] = 0 
        current_db.company.insert_one(x)
    x = current_db.company.find_one({"GlobalId": "global"})
    return render_template("refrence.html", company_data=x)

    

########################################################################


@calculations_bp.route('/company/update', methods=['GET', 'POST'])
@login_required
def update_company():
    """
    Update a company in the database
    """
    current_db = get_current_db()  
    print("current_db update", current_db)
    x = {}
    if request.method == "POST":
    
        x = get_form_to_dict(request.form)
        current_db.company.update_one({"GlobalId": "global"}, {"$set": x})
        x = current_db.company.find_one({"GlobalId": "global"})
    return redirect(url_for('calculation.company'))        
    return render_template("refrence.html", company_data=x)


####################################################################################

@calculations_bp.route('/company/delete', methods=['GET', 'POST'])
@login_required
def delete_company():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    print("current_db delete", current_db)    
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.company.delete_many({})
    return redirect(url_for('calculation.company'))        
    return render_template("refrence.html", company_data=x) 