import os
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()


def create_app(test_config=None):

    SmartSplitApp = Flask(__name__)

    if test_config is None:
        #app.config.from_pyfile('config.py', silent=True)
        basedir = os.path.abspath(os.path.dirname(__file__))
        SmartSplitApp.config.from_mapping(
            SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            SECRET_KEY = 'SuPeRsEcReT'
        )
    else:
        SmartSplitApp.config.from_mapping(test_config)

    db.init_app(SmartSplitApp)
    login.init_app(SmartSplitApp)
    login.login_view = 'login'

    # here are all the pieces of my program
    with SmartSplitApp.app_context():
        from . import routes, models
        db.create_all()

    return SmartSplitApp

