#pip install Flask-Restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class HelloPython(Resource):

    def get(self):
        return {'hello': 'Python Flask'}

api.add_resource(HelloPython, '/')        

if __name__ == '__main__':
    app.run(debug=True)

