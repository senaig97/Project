from flask import Flask
from config import Config

SmartSplitApp = Flask(__name__)
SmartSplitApp.config.from_object(Config)

from app import routes