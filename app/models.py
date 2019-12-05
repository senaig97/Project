from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

transactions = []

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Transaction:
    def __init__(self, total, people,  split):
        self.total = str(total)
        self.people = str(people)
        self.split = str(split)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
