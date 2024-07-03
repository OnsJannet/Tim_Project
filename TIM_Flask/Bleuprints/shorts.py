import imp
import logging
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
from Bleuprints.db_routes import db, client, get_current_db
import os
from dotenv import load_dotenv
load_dotenv()

shorts_bp = Blueprint('shorts', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = db



collection = db["shorts"]

@shorts_bp.route('/shorts', methods=['GET', 'POST'])
@login_required
def shorts():
    current_db = get_current_db()
    """
    Create new collection in the database
    """    
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i <13139):
        lst.append(("Short_Input" + str(i)))
        i += 1

    for entry in lst:
        x[entry] = 0                  
                                 
    current_db.shorts.insert_one(x)
    x = current_db.shorts.find_one({"GlobalId": "global"})
    return render_template("shorts.html", data=x)  

  


####################################################################################



@shorts_bp.route('/shorts/update', methods=['POST'])
@login_required
def shorts_update():
    current_db = get_current_db()
    """
    Update a company in the database
    """
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        current_db.shorts.update_one({"GlobalId": "global"}, {"$set": x})
    x =  current_db.shorts.find_one({"GlobalId": "global"})
    return redirect(url_for('shorts.shorts')) 
    return render_template("shorts.html", data=x)




####################################################################################

@shorts_bp.route('/shorts/delete',  methods=['POST'])
@login_required
def shorts_delete():
    current_db = get_current_db()
    """
    deletes a collection in the database
    """
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.shorts.delete_many({})
    return redirect(url_for('shorts.shorts'))    
    return render_template("tshorts.html", data=x)



