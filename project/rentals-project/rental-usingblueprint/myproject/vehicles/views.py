#Vehicles views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Vehicle
from myproject.vehicles.forms import AddForm, DelForm 
from flask_login import login_required

vehicles_blueprint = Blueprint('vehicles', __name__, template_folder='templates/vehicles')

@vehicles_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_vehicle():
    form = AddForm()

    if form.validate_on_submit():
        vehicle_number = form.vehicle_number.data
        vehicle_make   = form.vehicle_make.data
        vehicle_model  = form.vehicle_model.data
        vehicle_type   = form.vehicle_type.data
        vehicle_dop    = form.vehicle_dop.data
        owner_id       = form.owner_id.data

        # Add new vehicle to database
        new_vehicle = Vehicle(vehicle_number, vehicle_make, vehicle_model, vehicle_type, vehicle_dop, owner_id)
        db.session.add(new_vehicle)
        db.session.commit()

        return redirect(url_for('vehicles.all_vehicle'))

    return render_template('add_v.html', form=form)

@vehicles_blueprint.route('/vehicles')
@login_required
def all_vehicle():
    # Grab a list of vehicles from database.
    vehicles = Vehicle.query.all()
    return render_template('list_v.html', vehicles = vehicles)    

@vehicles_blueprint.route('/delete', methods=['GET', 'POST'])
@login_required
def del_vehicle():

    form = DelForm()

    if form.validate_on_submit():
        vehicle_id = form.vehicle_id.data
        vehicle = Vehicle.query.get(vehicle_id)
        db.session.delete(vehicle)
        db.session.commit()

        return redirect(url_for('vehicles.all_vehicle'))

    return render_template('delete_v.html',form=form)    