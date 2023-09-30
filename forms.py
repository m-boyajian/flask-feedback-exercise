from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class RegistrationForm(FlaskForm):
    """Form for registering user."""
    username = StringField("Username", validators=[InputRequired(), Length(min=6, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=30)])
    first_name = StringField("First Name", validators=[InputRequired(), Length(max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(max=30)])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])

class LoginForm(FlaskForm):
    """Form for user login."""
    username = StringField("Username", validators=[InputRequired(), Length(min=6, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=30)]) 

class FeedbackForm(FlaskForm):
    """Form for user feedback."""
    title = StringField("Title", validators=[InputRequired(), Length(max=100)])
    content = StringField("Content", validators=[InputRequired()]) 

class DeleteForm(FlaskForm):
    """Delete"""