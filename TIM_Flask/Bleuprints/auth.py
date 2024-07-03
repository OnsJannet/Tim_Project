import functools
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from models.user import User
from services.mongodb_interactions import get_form_to_dict
from datetime import datetime, timedelta
from services.emails_credencials import generate_login_credentials, send_login_by_mail, send_confirmation_by_mail
import os
from dotenv import load_dotenv
load_dotenv()

auth_bp = Blueprint('auth', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["TIM_Demo"]


@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    """Register a new user."""
    if request.method == 'POST':
        dic = get_form_to_dict(request.form)
        print(dic)
        user = User(dic)
        print(dic)
        error = None
        found = db.users.find_one({'email': dic["email"]})
        if not dic["username"]:
            error = 'Username is required.'
        elif not dic["password"]:
            error = 'Password is required'
        elif  found != None:
            error = 'Email already in use'

        if error is None:
                user.save()
                send_confirmation_by_mail(user.email, user.username)
                return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('auth.register'))

    return render_template('auth-register.html')


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db["users"].find_one({'email': email})

        if user is None:
            error = 'Incorrect email.'
        #elif not check_password_hash(user['password'], password):
        elif not user['password'] == password:
            error = 'Incorrect password.'

        if error == "":
            session.clear()
            session['user_id'] = user['_id']
            return redirect(url_for('admin.index'))

    return render_template('auth-login.html', error=error)

@auth_bp.route('/reset', methods=('GET', 'POST'))
def reset():
    if request.method == 'POST':
        email = request.form["email"]
        found = db.users.find_one({'email': email})
        if found:
            password = generate_login_credentials()
            db["users"].update_one(
                                {"email": email},
                                {"$set": {"password": password}}
                            )
            send_login_by_mail(email, found["username"], password)
            return redirect(url_for("auth.login"))
    return render_template("auth-forgot-password.html")

@auth_bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.users.find_one({'_id': user_id})


@auth_bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        if g.user and "trial" in g.user:
            if g.user["trial"] <= datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"):
                return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view