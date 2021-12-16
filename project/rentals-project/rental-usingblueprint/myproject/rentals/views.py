#Rentals views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Rental, Price
from myproject.rentals.forms import RentalForm, PriceForm
from flask_login import login_required

rentals_blueprint = Blueprint('rentals', __name__, template_folder='templates/rentals')

@rentals_blueprint.route('/rent', methods=['GET', 'POST'])
@login_required
def rental():
    form = RentalForm()

    if form.validate_on_submit():
        duration = form.duration.data
        vehicle_type = form.vehicle_type.data
        user_id  = form.user_id.data
        vehicle_id = form.vehicle_id.data

        #Fetch rent amount from price table
        rental = Price.query.filter(Price.vehicle_type==form.vehicle_type.data).filter(Price.duration==form.duration.data).first()
        #print(rental.amount)

        # Add new owner to database
        new_rental = Rental(duration, vehicle_type, user_id, vehicle_id, rental.amount)
        db.session.add(new_rental)
        db.session.commit()

        return redirect(url_for("rentals.thankyou"))

    return render_template('rental.html',form=form) 

@rentals_blueprint.route('/thankyou')   
@login_required
def thankyou():
    return render_template('thank_r.html')    

@rentals_blueprint.route('/rentallist') 
@login_required
def all_rental():
    # Grab a list of vehicles from database.
    rentals = Rental.query.all()
    return render_template('list_r.html', rentals = rentals)

@rentals_blueprint.route('/price', methods=['GET', 'POST'])
@login_required
def price():
    form = PriceForm()

    if form.validate_on_submit():
        vehicle_type = form.vehicle_type.data
        duration     = form.duration.data
        amount       = form.amount.data

        # Add new owner to database
        new_price = Price(vehicle_type, duration, amount)
        db.session.add(new_price)
        db.session.commit()

        return redirect(url_for("rentals.all_price"))

    return render_template('price.html',form=form)    

@rentals_blueprint.route('/priceslist')
@login_required
def all_price():
    # Grab a list of vehicles from database.
    prices = Price.query.all()
    return render_template('list_p.html', prices = prices) 