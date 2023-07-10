from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, logout_user, login_manager, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'anythingispossible'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        create_database()
    
    return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()

    