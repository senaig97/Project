from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class EditCredsForm(FlaskForm):
    newUsername = StringField('New Username')
    newPassword = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')
   
class SplitForm(FlaskForm):
    amount = IntegerField('Amount')
    people = IntegerField('People')
