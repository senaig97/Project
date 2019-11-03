# NOTE
# Most of this is just to test if Register works since the main app py file isn't up yet
# Things to do include username/password/email validation, and setup of the database

from flask import Flask, render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')


#   def validate_username(self, username):
#       user = User.query.filter_by(username=username.data).first()
#       if user is not None:
#           raise ValidationError('Username already taken')

#   def validate_email(self, email):
#       user = User.query.filter_by(email=email.data).first()
#       if user is not None:
#           raise ValidationError('Email address already taken')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'


@app.route('/')
def register():
    form = RegistrationForm()

    return render_template('Register.html', form=form)


if __name__ == '__main__':
    app.run()
