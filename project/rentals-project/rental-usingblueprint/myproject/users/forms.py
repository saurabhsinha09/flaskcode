from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class AddForm(FlaskForm):

    name   = StringField('Name of User:')
    email  = StringField('Email ID:')
    submit = SubmitField('Add User') 

class DelForm(FlaskForm):

    user_id  = IntegerField('Id of user to Remove:')
    submit   = SubmitField('Remove user')    