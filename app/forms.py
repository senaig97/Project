from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    # Code related to log in to go here
    print('Log in')

class EditCredsForm(FlaskForm):
    newUsername = StringField('New Username')
    newPassword = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')