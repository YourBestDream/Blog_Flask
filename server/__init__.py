import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = f'{os.environ.get("SECRET_KEY")}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.environ.get("POSTGRES_USERNAME")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_URL")}/{os.environ.get("POSTGRES_DATABASE")}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app

