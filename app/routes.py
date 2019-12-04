from app import SmartSplitApp, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import EditCredsForm, LoginForm, SplitForm, RegistrationForm, SurveyForm
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse


@SmartSplitApp.route('/')
@SmartSplitApp.route('/home')
def home():
    return render_template("Home.html")


@SmartSplitApp.route("/login", methods=["GET", "POST"])
def login():
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
    logout_user()
    return redirect(url_for('home'))


@SmartSplitApp.route('/register', methods=['GET', 'POST'])
def register():
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


@SmartSplitApp.route('/evensplit', methods=['GET', 'POST'])
def evensplit():
    form = SplitForm()
    # print(form.validate_on_submit())
    # print(form.errors)
    # print(form.amount.data, form.people.data)
    # if form.validate_on_submit() and request.method == 'POST':
    #     a = form.amount.data
    #     p = form.people.data
    #     s = a // p
    #     print(s)
    #     flash(s, 'result')
    # else:
    #     return render_template('EvenSplit.html', form=form)

    result = None
    if request.method == 'POST':
        if form.validate_on_submit():
            number = float(form.amount.data)
            divide_by = float(form.people.data)
            result = str(number / divide_by)
            print(result)
    return render_template('EvenSplit.html', title='Even Split', form=form, result=result)

@SmartSplitApp.route('/evensplit2', methods=['POST', 'GET'])
def evensplit2():
    if request.method == 'POST':
        cst = float(request.form['cost'])
        ppl = float(request.form['people'])
        if ppl == 0:
            result = 'Cannot divide by zero'
        else:
            result = str(cst/ppl)
        return render_template('evensplit2.html', result=result)
    if request.method == 'GET':
        result = 'undefined'
        return render_template('evensplit2.html', result=result)

@SmartSplitApp.route('/rating')
def rating():
    return render_template('rating.html')

@SmartSplitApp.route('/survey')
def survey():
    form = SurveyForm(request.form)
    if form.validate_on_submit() and request.method == 'POST':
        flash('Thank you for taking our survey, your feedback is appreciated')
        return redirect(url_for('home'))
    return render_template('survey.html', form = form)


@SmartSplitApp.route('/aboutUs')
def aboutUs():
    return render_template('AboutUs.html')
