#################
####HTML#########
#################
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class SignupForm(FlaskForm):

    name   = StringField('Name of Owner:')
    email  = StringField('Email ID:')
    submit = SubmitField('Add Owner')

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

class DelownerForm(FlaskForm):

    owner_id = IntegerField('Id of owner to Remove:')
    submit   = SubmitField('Remove owner')    

class PriceForm(FlaskForm):

    vehicle_type = SelectField(u'Type of vehicle', choices = [('car', '4-wheeler'), ('bike', '2-wheeler')])
    duration     = SelectField(u'Rental duration', choices = [('day', 'Day'), ('week', 'Week'), ('month', 'Month')])
    amount       = IntegerField('Rental Amount:')
    submit       = SubmitField('Add price details')      

class UserForm(FlaskForm):

    name   = StringField('Name of User:')
    email  = StringField('Email ID:')
    submit = SubmitField('Add User')    

class RentalForm(FlaskForm):
    
    duration     = SelectField(u'Rental duration', choices = [('day', 'Day'), ('week', 'Week'), ('month', 'Month')])
    vehicle_type = SelectField(u'Type of vehicle', choices = [('car', '4-wheeler'), ('bike', '2-wheeler')])
    user_id      = IntegerField('ID of user:')
    vehicle_id   = IntegerField('ID of vehicle:')
    submit       = SubmitField('Rental Vehicle')

class DeluserForm(FlaskForm):

    user_id  = IntegerField('Id of user to Remove:')
    submit   = SubmitField('Remove user')    