#Owners form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class AddForm(FlaskForm):

    name   = StringField('Name of Owner:')
    email  = StringField('Email ID:')
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):

    owner_id = IntegerField('Id of owner to Remove:')
    submit   = SubmitField('Remove owner')     