from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField

class LoginForm(Form):
    username = StringField('Username', [
            validators.Required(),
            validators.Length(min=4, max=25)
        ])
    password = PasswordField('Password', [
            validators.Required(),
            validators.Length(min=4, max=80)
        ])

class PostForm(Form):
    title = StringField('Title', [
        validators.Required(),
        validators.Length(max=80)
    ])
    body = TextAreaField('Body', validators=[validators.Required()])