from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class RentalForm(FlaskForm):
    
    duration     = SelectField(u'Rental duration', choices = [('day', 'Day'), ('week', 'Week'), ('month', 'Month')])
    vehicle_type = SelectField(u'Type of vehicle', choices = [('car', '4-wheeler'), ('bike', '2-wheeler')])
    user_id      = IntegerField('ID of user:')
    vehicle_id   = IntegerField('ID of vehicle:')
    submit       = SubmitField('Rental Vehicle')

class PriceForm(FlaskForm):

    vehicle_type = SelectField(u'Type of vehicle', choices = [('car', '4-wheeler'), ('bike', '2-wheeler')])
    duration     = SelectField(u'Rental duration', choices = [('day', 'Day'), ('week', 'Week'), ('month', 'Month')])
    amount       = IntegerField('Rental Amount:')
    submit       = SubmitField('Add price details')     