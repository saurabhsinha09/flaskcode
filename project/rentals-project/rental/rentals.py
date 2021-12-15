####################
####View/DB Form####
####################
import os
from rentals_form import  SignupForm, AddForm , DelForm, DelownerForm, DeluserForm, PriceForm, UserForm, RentalForm
from flask import Flask, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'carbikerental'

############################################
        # SQL DATABASE AND MODELS
##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rentals.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mysql1234@localhost/rentals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Owner(db.Model):

    __tablename__ = 'owners'
    owner_id = db.Column(db.Integer,primary_key= True)
    name     = db.Column(db.Text)
    email    = db.Column(db.String(120))
    #Every owner can have one vehicle
    vehicles = db.relationship('Vehicle', backref = 'vehicle', uselist=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        if self.vehicles:
            return f"Owner name is {self.name}, owner id is {self.owner_id} and vehicle number is {self.vehicles.vehicle_number}."
        else:
            return f"Owner name is {self.name}, email-id is {self.email} and owner id is {self.owner_id}."

class Vehicle(db.Model):

    __tablename__ = 'vehicle'
    vehicle_id     = db.Column(db.Integer,primary_key = True)
    vehicle_number = db.Column(db.Text)
    vehicle_make   = db.Column(db.Text)
    vehicle_model  = db.Column(db.Text)
    vehicle_type   = db.Column(db.Text)
    vehicle_dop    = db.Column(db.Text)
    # use owners.owner_id because __tablename__='owners'
    owner_id       = db.Column(db.Integer, db.ForeignKey('owners.owner_id'))

    def __init__(self, vehicle_number, vehicle_make, vehicle_model, vehicle_type, vehicle_dop, owner_id):
        self.vehicle_number = vehicle_number
        self.vehicle_make   = vehicle_make
        self.vehicle_model  = vehicle_model
        self.vehicle_type   = vehicle_type
        self.vehicle_dop    = vehicle_dop
        self.owner_id       = owner_id

    def __repr__(self):
        return f"{self.vehicle_id} - Vehicle number is {self.vehicle_number}, type is {self.vehicle_type} and owner id is {self.owner_id}."

class Price(db.Model):

    __tablename__ = 'price'
    type_id      = db.Column(db.Integer,primary_key= True)
    vehicle_type = db.Column(db.Text)
    duration     = db.Column(db.Text)
    amount       = db.Column(db.Integer)
    
    def __init__(self, vehicle_type, duration, amount):
        self.vehicle_type = vehicle_type
        self.duration     = duration
        self.amount       = amount

    def __repr__(self):
        return f"Rental amount for vehicle type {self.vehicle_type} of duration {self.duration} is {self.amount}." 

class User(db.Model):

    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key= True)
    name    = db.Column(db.Text)
    email   = db.Column(db.String(120))
    #Every user can rent one vehicle
    rental = db.relationship('Rental', backref = 'vehicle', uselist=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        if self.rental:
            return f"User name is {self.name} and user id is {self.user_id} has rented vehicle id {self.rental.vehicle_id}."
        else:
            return f"User name is {self.name} and user id is {self.user_id} has not rented any vehicle."

class Rental(db.Model):

    __tablename__ = 'rental'
    rental_id     = db.Column(db.Integer,primary_key = True)
    duration      = db.Column(db.Text)
    vehicle_type  = db.Column(db.Text)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    vehicle_id    = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'))
    rental        = db.Column(db.Integer)

    def __init__(self, duration, vehicle_type, user_id, vehicle_id, rental):
        self.duration     = duration
        self.vehicle_type = vehicle_type
        self.user_id      = user_id
        self.vehicle_id   = vehicle_id
        self.rental       = rental

    def __repr__(self):
        return f"The rental for {self.vehicle_id} of type {self.vehicle_type} for duration {self.duration} is {self.rental}"      

############################################
        # VIEWS WITH FORMS
##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Add new owner to database
        new_owner = Owner(name, email)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("thankyou"))

    return render_template('signup.html',form=form)

@app.route('/thankyou')    
def thankyou():
    return render_template('thankyou.html')  

@app.route('/add', methods=['GET', 'POST'])
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

        return redirect(url_for('all_vehicle'))

    return render_template('add.html', form=form)

@app.route('/vehicleslist')
def all_vehicle():
    # Grab a list of vehicles from database.
    vehicles = Vehicle.query.all()
    return render_template('listall.html', vehicles = vehicles)    

@app.route('/ownerslist')
def all_owner():
    # Grab a list of vehicles from database.
    owners = Owner.query.all()
    return render_template('listall.html', owners = owners)     

@app.route('/userslist')
def all_user():
    # Grab a list of vehicles from database.
    users = User.query.all()
    return render_template('listall.html', users = users)    

@app.route('/rentallist')
def all_rental():
    # Grab a list of vehicles from database.
    rentals = Rental.query.all()
    return render_template('listall.html', rentals = rentals)     

@app.route('/deletevehicle', methods=['GET', 'POST'])
def del_vehicle():

    form = DelForm()

    if form.validate_on_submit():
        vehicle_id = form.vehicle_id.data
        vehicle = Vehicle.query.get(vehicle_id)
        db.session.delete(vehicle)
        db.session.commit()

        return redirect(url_for('all_vehicle'))

    return render_template('delete.html',form=form)

@app.route('/deleteowner', methods=['GET', 'POST'])
def del_owner():

    form = DelownerForm()

    if form.validate_on_submit():
        owner_id = form.owner_id.data
        owner = Owner.query.get(owner_id)
        db.session.delete(owner)
        db.session.commit()

        return redirect(url_for('all_owner'))

    return render_template('deleteo.html',form=form)

@app.route('/deleteuser', methods=['GET', 'POST'])
def del_user():

    form = DeluserForm()

    if form.validate_on_submit():
        user_id = form.user_id.data
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('all_user'))

    return render_template('deleteu.html',form=form)

@app.route('/priceslist')
def all_price():
    # Grab a list of vehicles from database.
    prices = Price.query.all()
    return render_template('listall.html', prices = prices)         

@app.route('/price', methods=['GET', 'POST'])
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

        return redirect(url_for("all_price"))

    return render_template('price.html',form=form)

@app.route('/user', methods=['GET', 'POST'])
def usersignup():
    form = UserForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Add new owner to database
        new_user = User(name, email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("thankyou"))

    return render_template('user.html',form=form)    

@app.route('/rental', methods=['GET', 'POST'])
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

        return redirect(url_for("thankyou"))

    return render_template('rental.html',form=form)     

if __name__ == '__main__':
    app.run(debug=True)