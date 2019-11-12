from app import myFlaskObj
from flask import render_template
from form import LoginForm
from flask import flash

@myFlaskObj.route('/')
def home():
    return render_template('Home.html, form = form')

@myFlaskObj.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You are logged in')
    return render_template('LogIn.html', form = form)
