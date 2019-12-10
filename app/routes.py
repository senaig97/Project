from app import db
from flask import current_app as SmartSplitApp
from flask import render_template, flash, redirect, url_for, request
from app.forms import EditCredsForm, LoginForm, RegistrationForm, SurveyForm
from app.models import User, transactions, Transaction
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse


@SmartSplitApp.route('/')
@SmartSplitApp.route('/home')
def home():
    """Home page for SmartSplit. The homepage includes all the options available to user once they go to the website."""
    return render_template("Home.html")


@SmartSplitApp.route("/login", methods=["GET", "POST"])
def login():
    """Log in page for SmartSplit. Asks for the username and password. After clicking on submit/ login : redirects
    user to the hoempage. """
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')

        return redirect(next_page)
    return render_template('LogIn.html', title='Log in', form=form)


@SmartSplitApp.route("/logout")
def logout():
    """Logs the user out. The user still stays on the homepage but is not logged into their account anymore."""
    logout_user()
    return redirect(url_for('home'))


@SmartSplitApp.route('/register', methods=['GET', 'POST'])
def register():
    """Uses the database file to store credential information. Username, password, confirm password and submit fields
    are used. Once registered, the information is saved locally """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@SmartSplitApp.route('/editCredentials', methods=["GET", "POST"])
@login_required
def editCredentials():
    """Allows user to change their password. Requires a user to have already been logged in. If not already logged
    in, redirects user to login screen. Else, redirects user to home screen when new password is submitted. """
    form = EditCredsForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(id=current_user.id).first()
            user.set_password(form.newPassword.data)
            db.session.add(user)
            db.session.commit()
            flash('Credentials successfully edited')
            return redirect(url_for('login'))
    return render_template('editCredentials.html', title='Edit Credentials', form=form)

@SmartSplitApp.route('/evensplit', methods=['POST', 'GET'])
def evensplit():
    """Basic split option. User inputs total cost, number of people involved, and a comment. Shows the split cost as
    total cost divided by number of people. Posts the transaction w/ username, total cost, # people, and comment on
    the History page. """
    if request.method == 'POST':
        cst = float(request.form['cost'])
        ppl = float(request.form['people'])
        cmt = request.form['comment']
        if ppl == 0:
            result = 'Cannot divide by zero'
        else:
            result = "$" + str(cst/ppl)
            transactions.append(Transaction(cst, ppl, cst/ppl, current_user.username, cmt))
        return render_template('evensplit.html', result=result)
    if request.method == 'GET':
        result = ' '
        return render_template('evensplit.html', result=result)

@SmartSplitApp.route('/history')
def history():
    """Displays transactions in order of username, total cost, # people, and comment."""
    return render_template('History.html', transactions=transactions)

@SmartSplitApp.route('/rating')
def rating():
    """The link helps get feedback from the user. It directs users to a page where they can rate the app accordingly."""
    return render_template('rating.html')

@SmartSplitApp.route('/survey')
def survey():
    """Presents a survey to be filled out by the user."""
    form = SurveyForm(request.form)
    if form.validate_on_submit() and request.method == 'POST':
        flash('Thank you for taking our survey, your feedback is appreciated')
        return redirect(url_for('home'))
    return render_template('survey.html', form = form)


@SmartSplitApp.route('/aboutUs')
def aboutUs():
    """Displays additional information about the site."""
    return render_template('AboutUs.html')
