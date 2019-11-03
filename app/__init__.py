from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

SmartSplitApp = Flask(__name__)
SmartSplitApp.config.from_object(Config)

db = SQLAlchemy(SmartSplitApp)

from app import routes, models
