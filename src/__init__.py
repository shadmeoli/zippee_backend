from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
db = SQLAlchemy()


def create_app():
    app.config['SECRET_KEY'] = "abcd"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:password@localhost/zippee'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'jitesharora003@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Iwillbeback002'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    db.init_app(app)
    from .views import views
    from .auth import auth
    from .mail import send_mail
    with app.app_context():
        db.create_all()
    app.register_blueprint(send_mail, url_prefix="/api")
    app.register_blueprint(views, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/api")
    from .models import Users, Notifications

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        return {"data": "login first"}

    return app


def create_database(app):
    if not path.exists('src/zippee.db'):
        db.create_all()
        print("Database Create")
