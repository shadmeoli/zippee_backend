from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(20))
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_date = db.Column(db.DateTime(timezone=True), default=func.now())
    notification_id = db.relationship('Notifications')