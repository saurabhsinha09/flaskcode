
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import configparser

config = configparser.ConfigParser()
config.read('./myproject/db.ini')
host   = config['pgsql']['host']
user   = config['pgsql']['user']
passwd = config['pgsql']['passwd']
db     = config['pgsql']['db']

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'carbikerental'

############################################
        # SQL DATABASE #
##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rentals.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+user+':'+passwd+'@'+host+'/'+db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from myproject.owners.views   import owners_blueprint
from myproject.vehicles.views import vehicles_blueprint
from myproject.users.views    import users_blueprint
from myproject.rentals.views  import rentals_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(vehicles_blueprint, url_prefix='/vehicles')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(rentals_blueprint, url_prefix='/rentals')