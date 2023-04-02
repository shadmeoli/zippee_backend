import json
from datetime import datetime

from flask_mail import Mail, Message
from flask import Blueprint, request, send_file
from . import app, db, common
from .models import Users, Notifications

mail = Mail(app)

send_mail = Blueprint('mail', __name__)


@send_mail.route("/mail/send", methods=["POST"])
def send_notifications():
    data = json.loads(request.data)
    html_body = data.get('body')
    subject = data.get("subject")
    users = Users.query.all()
    # Implement Async and add Try except
    for user in users:
        html_body = common.email_tracker_body.format(id=user.id)
        msg = Message(
            subject,
            sender='jitesharora003@gmail.com',
            recipients=[user.email],
            html=html_body
        )
        print(mail.send(msg))
        notification = Notifications(user_id=user.id, data=str(data))
        print(notification)
        db.session.add(notification)
    db.session.commit()
    return {"status": True, "message": "Success"}, 200

@send_mail.route("/mail/tracker", methods=["GET"])
def email_opened_webhook():
    data = request.args
    notification = Notifications.query.get(data.get('id'))
    notification.read_at = datetime.now()
    db.session.commit()
    return send_file('static/zippee.png', 'image/gif')
