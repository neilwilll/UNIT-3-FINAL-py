from wtforms import PasswordField, StringField, validators
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
   username = StringField('Username', [validators.InputRequired()])
   password = PasswordField('Password', [validators.InputRequired()])