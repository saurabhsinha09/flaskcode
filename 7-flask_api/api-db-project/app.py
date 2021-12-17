import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource,reqparse
from user_check import authenticate,identity
from flask_jwt import JWT ,jwt_required
from flask_migrate import Migrate

app = Flask(__name__)

###################################################
################ CONFIGURATIONS ###################
##################################################
app.config['SECRET_KEY'] = 'dcn'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'user.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
jwt = JWT(app, authenticate, identity)
api = Api(app)

###################################################
################ MODELS ###########################
##################################################
class Users(db.Model):
    name   = db.Column(db.String(80),primary_key=True)
    gender = db.Column(db.String(2))

    def __init__(self,name,gender):
        self.name   = name
        self.gender = gender

    def json(self):
        return {'name': self.name, 'gender': self.gender}

    def __str__(self):
        return f"{self.name, self.gender} "

###################################################
################ RESOURCES ########################
###################################################
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('gender', type=str)

class UserResource(Resource):
    def get(self):
        
        args = parser.parse_args()
        name = args['name']
        user = Users.query.filter_by(name=name).first()

        if user:
            return user.json()
        else:
            # If you request a user not yet in the users list
            return {'name':'not found'}, 404

    def post(self):
        
        args = parser.parse_args()
        name = args['name']
        gender = args['gender']
        user = Users(name=name, gender=gender)
        db.session.add(user)
        db.session.commit()

        return user.json()

    def put(self):
        
        args = parser.parse_args()
        name = args['name']
        gender = args['gender']
        user = Users.query.filter_by(name=name).first()
        user.gender = gender
        db.session.commit()

        return user.json()

    def delete(self):
        
        args = parser.parse_args()
        name = args['name']
        user = Users.query.filter_by(name=name).first()
        db.session.delete(user)
        db.session.commit()

        return {'note':'delete successful'}

class AllUsers(Resource):

    @jwt_required()
    def get(self):
        # return all the users :)
        users = Users.query.all()

        # return json of (users)
        return [user.json() for user in users]

api.add_resource(UserResource, '/user')
api.add_resource(AllUsers,'/users')

if __name__ == '__main__':
    app.run(debug=True)
