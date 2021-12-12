import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:Test12345@localhost/db1'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:Test1234@localhost/db1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
#####################################
# Let's create our first model!
# We inherit from db.Model class
class Users(db.Model):

    # If you don't provide this, the default table name will be the class name
    __tablename__ = 'users'

    # Now create the columns
    # Full docs: http://docs.sqlalchemy.org/en/latest/core/types.html

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each user
    id = db.Column(db.Integer,primary_key=True)
    # User name
    name = db.Column(db.Text)
    # User age in years
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)

    # This sets what an instance in this table will have
    # Note the id will be auto-created.
    def __init__(self,name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        # This is the string representation of a user details in the model
        return f"User {self.name} is {self.age} years old of gender {self.gender}."
