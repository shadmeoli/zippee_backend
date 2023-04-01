import json

from flask_mail import Mail, Message
from flask import Blueprint, request
from . import app
from .models import Users

mail = Mail(app)

send_mail = Blueprint('mail', __name__)


@send_mail.route("/send", methods=["POST"])
def send_notifications():
    data = json.loads(request.data)
    html_body = data.get('body')
    subject = data.get("subject")
    users = Users.query.all()
    # Implement Async
    for email in users.email:
        msg = Message(
            subject,
            sender='jitesharora003@gmail.com',
            recipients=[email],
            html=html_body
        )
        mail.send(msg)
    return 'Sent'
