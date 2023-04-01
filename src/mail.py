import json
from datetime import datetime

from flask_mail import Mail, Message
from flask import Blueprint, request
from . import app, db
from .models import Users, Notifications

mail = Mail(app)

send_mail = Blueprint('mail', __name__)


@send_mail.route("/send", methods=["POST"])
def send_notifications():
    data = json.loads(request.data)
    html_body = data.get('body')
    subject = data.get("subject")
    users = Users.query.all()
    # Implement Async and add Try except
    for user in users:
        msg = Message(
            subject,
            sender='jitesharora003@gmail.com',
            recipients=[user.email],
            html=html_body
        )
        mail.send(msg)
        Notifications(email=user.email, user_id=user.id, data=data)



@send_mail.route("/opened", methods=["GET"])
def email_opened_webhook():
    data = json.loads(request.data)
    notification = Notifications.query.get(data.get("id"))
    notification.read_at = datetime.now()
    db.session.commit()