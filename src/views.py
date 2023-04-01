from flask import Blueprint
from flask_login import login_required, login_manager

views = Blueprint('views', __name__)

@views.route("/")
@login_required
def home():
    return {"message": "homepage"}



