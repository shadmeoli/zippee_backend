import json

from flask import Blueprint, request
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import Users
from flask_login import login_user, login_required, logout_user
auth = Blueprint('auth', __name__)



@auth.route("/login", methods=["POST"])
@cross_origin()
def login():
    data = json.loads(request.data)
    email = data.get('email')
    password = data.get('password')
    user = Users.query.filter_by(email=email).first()

    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return {"email": email, "name": user.name, "created_at": user.created_date}, 200
        else:
            return {"message": "Invalid Password"}, 401
    else:
        return {"message": "user doesn't exist. Please Signup"}, 401


@auth.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    data = json.loads(request.data)
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    comfirmed_password = data.get("cpassword")
    if comfirmed_password != password:
        return {"message": "Passwords didn't match"}, 401
    user = Users.query.filter_by(email=email).first()

    if user:
        return {"message": "User already exist."}
    new_user = Users(email=email, password=generate_password_hash(password, method="sha256"), name=name)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)
    return {"email": email, "password": password}, 200


@auth.route("/logout")
@login_required
@cross_origin()
def logout():
    logout_user()
    return {"status": True, "message": "User is logged out"}



@auth.route("/notification")
def notification_opend():
    return {"status": True, "data": "notification_opend"}



