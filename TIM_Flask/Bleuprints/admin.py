import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
import os
from dotenv import load_dotenv
load_dotenv()


admin_bp = Blueprint('admin', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["TIM_Demo"]

@admin_bp.route('/index')
@login_required
def index():
    """Admin index page"""
    dic = db["users"].find_one({"_id": session['user_id']})
    user = User(dic)
    
    print(user.username)
    return render_template('dashboard-manager.html', user=user)





@admin_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Admin profile page"""
    dic = db["users"].find_one({"_id": session['user_id']})
    user = User(dic)
    user_id = session['user_id']
    username = db['users'].find_one({"_id": user_id})["username"]
    attributes = ["name", "surname", "email", "organization", "phoneNumber",
                  "address", "state", "zip_code",
                  "country"]
    if request.method == "POST":
        data = {}
        for x in attributes:
            if x in request.form:
                if request.form[x] != '':
                    data[x] = request.form[x]
            else:
                data[x] = None
        db["users"].update_one({'_id': session['user_id']}, {"$set": data});
        return redirect(url_for('admin.profile'))
    found = db["users"].find_one({'_id': session['user_id']})
    data = {}
    for x in attributes:
        if x in found:
            data[x] = found[x]
        else:
            data[x] = None
    return render_template('page-account-settings-account.html', data=data, username=username, user=user)

