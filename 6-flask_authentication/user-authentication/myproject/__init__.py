import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dcn'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#Pass in our app to the login manager
login_manager.init_app(app)

#View to go to when they need to login.
login_manager.login_view = "login"