
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import configparser
from flask_restful import Api
from flask_marshmallow import Marshmallow

config = configparser.ConfigParser()
config.read('./myproject/db.ini')
host   = config['pgsql']['host']
user   = config['pgsql']['user']
passwd = config['pgsql']['passwd']
db     = config['pgsql']['db']

# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'carbikerental'

ma = Marshmallow(app)

############################################
        # SQL DATABASE #
##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rentals.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+user+':'+passwd+'@'+host+'/'+db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#Pass in our app to the login manager
login_manager.init_app(app)

#View to go to when they need to login.
login_manager.login_view = "login.login"

from myproject.owners.views   import owners_blueprint
from myproject.vehicles.views import vehicles_blueprint
from myproject.users.views    import users_blueprint
from myproject.rentals.views  import rentals_blueprint
from myproject.login.views    import login_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(vehicles_blueprint, url_prefix='/vehicles')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(rentals_blueprint, url_prefix='/rentals')
app.register_blueprint(login_blueprint, url_prefix='/login')

from myproject.resources.routes import initialize_routes
api = Api(app)
initialize_routes(api)