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

items_bp = Blueprint('items', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["items"]

@items_bp.route('/items', methods=['GET', 'POST'])
@login_required
def items():
    """
    Create new collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        print(x)
        x['GlobalId'] = 'global' 
        
    x = current_db.items.find()
    
    return render_template("items.html", data=x)  

        #######################################


@items_bp.route('/items/add', methods=['GET', 'POST'])
@login_required
def add_items():
    """
    Create new collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        print(x)
        x['GlobalId'] = 'global' 
        
        current_db.items.insert_one(x)
    x = current_db.items.find()
    return redirect(url_for('items.items'))    
    return render_template("items.html", data=x)       



####################################################################################



@items_bp.route('/items/update', methods=['POST'])
@login_required
def items_update():
    """
    Update a company in the database
    """
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        current_db.items.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.items.find_one({"GlobalId": "global"})
    return redirect(url_for('items.items')) 
    return render_template("items.html", data=x) 




####################################################################################

@items_bp.route('/items/delete',  methods=['POST'])
@login_required
def items_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.items.deleteOne({"_id": args["id"]})
    return redirect(url_for('items.items'))    
    return render_template("items.html", data=x) 

