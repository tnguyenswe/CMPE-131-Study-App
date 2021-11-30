from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    signup=SubmitField("Sign Up")

class UploadForm(FlaskForm):
    file = FileField()

class ToDoForm(FlaskForm):
    todo=StringField('Start building your to-do list!',validators=[DataRequired()])
    submit=SubmitField()

class SearchTextForm(FlaskForm):
    input_file = FileField('Upload', validators=[FileRequired()])
    text = StringField('Search Text', validators=[DataRequired()])
    search = SubmitField('Search')
