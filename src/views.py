from flask import Blueprint
from flask_login import login_required, login_manager

views = Blueprint('views', __name__)


@views.route("/home")
@login_required
def home():
    return {"status": True, "message": "Welcome!!!"}
