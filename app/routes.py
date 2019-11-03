from app import SmartSplitApp
from flask import render_template
from app.forms import EditCredsForm


@SmartSplitApp.route('/')
def logIn():
    # code related to log in to go here
    username = None


@SmartSplitApp.route('/editCredentials')
def editCredentials():
    form = EditCredsForm()
    if form.validate_on_submit():
        pass
    return render_template('editCredentails.html', form=form)
