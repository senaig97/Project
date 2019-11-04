from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, validators
# from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    # code for registration to go here
    print('Please register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class EditCredsForm(FlaskForm):
    newUsername = StringField('New Username')
    newPassword = PasswordField('New Password', validators=[
        validators.data_required(),
        validators.equal_to('confirm', message='Passwords must match')
    ])
    submit = SubmitField('Repeat Password')


class SplitForm(FlaskForm):
    amount = IntegerField('Amount')
    people = IntegerField('People')
