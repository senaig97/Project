from app import SmartSplitApp
from flask import request, session, redirect, url_for, render_template, flash, g
from flask import app
from app.forms import EditCredsForm, LoginForm, SplitForm, RegistrationForm

@SmartSplitApp.route("/")


@SmartSplitApp.route("/home")
def home():
    return render_template("Home.html")


@SmartSplitApp.route('/register')
def register():
    form = RegistrationForm()
    return render_template('Register.html', form=form)


@SmartSplitApp.route("/login", methods=["GET", "POST"])
def login():
    g.selected_tab = "login"

    form = LoginForm()
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            error = "Invalid login credentials"
        elif request.form["password"] != app.config["PASSWORD"]:
            error = "Invalid login credentials"
        else:
            session["logged_in"] = True
            flash("You are logged in")
            if session.get("project"):
                return redirect(url_for("home"))
            return redirect(url_for("projects"))

    return render_template("LogIn.html", form=form)


@SmartSplitApp.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("projects"))


@SmartSplitApp.route('/editcredentials', methods=["GET", "POST"])
def editcredentials():
    form = EditCredsForm()
    if form.validate_on_submit():
        pass
    return render_template('editCredentails.html', form=form)


@SmartSplitApp.route('/smartsplit')
def smartsplit():
    # code for smart split to go here
    form = SplitForm()
