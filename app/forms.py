from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, NumberRange
from app.models import User


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
    amount = FloatField('cost')
    people = IntegerField('people', validators=[NumberRange(min=1)])
    splitbill = FloatField('splitbill')


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
