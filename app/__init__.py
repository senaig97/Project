from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

SmartSplitApp = Flask(__name__)
SmartSplitApp.config.from_object(Config)

db = SQLAlchemy(SmartSplitApp)

login = LoginManager(SmartSplitApp)

login.login_view = 'login'

from app import routes, models
