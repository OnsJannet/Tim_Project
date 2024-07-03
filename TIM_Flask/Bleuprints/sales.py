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

sales_bp = Blueprint('sales', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["sales"]

@sales_bp.route('/add_invoice', methods=['GET', 'POST'])
@login_required
def add_invoice():
    """
    Create new collection in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        print(x)
        x['GlobalId'] = 'global' 
        
        current_db.sales.insert_one(x)
    x = current_db.sales.find_one({"GlobalId": "global"})
    return render_template("app-invoice-add.html", data=x)

####################################################################################

@sales_bp.route('/add_invoice/update', methods=['POST'])
@login_required
def add_invoice_update():
    """
    Update a company in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        current_db.sales.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.sales.find_one({"GlobalId": "global"})
    return redirect(url_for('sales.sales')) 
    return render_template("app-invoice-add.html", data=x)



####################################################################################

@sales_bp.route('/add_invoice/delete', methods=['GET', 'POST'])
@login_required
def add_invoice_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'   
        x= current_db.sales.delete_many({})
    return redirect(url_for('sales.sales'))
    return render_template("app-invoice-add.html", data=x)