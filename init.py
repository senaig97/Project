from flask import Flask
from config import Config

myFlaskObj = Flask(__name__)
myFlaskObj.config.from_object(Config)

from app import routes
