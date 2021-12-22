##db setup inside __init__.py##
from myproject import db, login_manager, ma
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

# The user_loader decorator allows flask-login  
# to load the current user and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(user_id)

class Login(db.Model, UserMixin):

    __tablename__ = 'login'
    id            = db.Column(db.Integer, primary_key = True)
    email         = db.Column(db.String(64), unique=True, index=True)
    username      = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email         = email
        self.username      = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

class Owner(db.Model):

    __tablename__ = 'owners'
    owner_id = db.Column(db.Integer,primary_key= True)
    name     = db.Column(db.Text)
    email    = db.Column(db.String(120),unique=True, index=True)
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

class PriceSchema(ma.Schema):
    class Meta:
        fields = ('type_id','vehicle_type','duration','amount')

class User(db.Model):

    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key= True)
    name    = db.Column(db.Text)
    email   = db.Column(db.String(120),unique=True, index=True)
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
        return f"The rental for {self.vehicle_id} of type {self.vehicle_type} for duration {self.duration} is {self.rental}."