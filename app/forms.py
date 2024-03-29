from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, NumberRange
from app.models import User
from flask_login import current_user


class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class EditCredsForm(FlaskForm):
    newPassword = PasswordField('New Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('newPassword')])
    submit = SubmitField('Confirm')

    def validate_password(self, newPassword):
        if not current_user.check_password(newPassword.data):
            raise ValidationError("Please use a new password.")


class SplitForm(FlaskForm):
    amount = FloatField('Total Cost')
    people = FloatField('# of people', validators=[NumberRange(min=1)])
    submit = SubmitField('Calculate')



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
            
class SurveyForm(FlaskForm):
    submit = SubmitField('Submit!')
