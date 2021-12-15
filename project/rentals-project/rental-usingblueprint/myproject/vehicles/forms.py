#Vehicles form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class AddForm(FlaskForm):

    vehicle_number = StringField('Your Vehicle Number:')
    vehicle_make   = StringField('Brand of your vehicle:')
    vehicle_model  = StringField('Model of vehicle:')
    vehicle_type   = SelectField(u'Type of vehicle', choices = [('car', '4-wheeler'), ('bike', '2-wheeler')])
    vehicle_dop    = StringField('Date of Purchase:')
    owner_id       = IntegerField('ID of owner:')
    submit         = SubmitField('Add Vehicle')

class DelForm(FlaskForm):

    vehicle_id = IntegerField('Id of vehicle to Remove:')
    submit     = SubmitField('Remove vehicle')