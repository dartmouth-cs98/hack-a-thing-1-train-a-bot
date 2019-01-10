from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from chat import Chat
# from flask.ext.jsonpify import jsonify

# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('key')
chatbot = Chat()

class Employees(Resource):
    def get(self):
        # conn = db_connect.connect() # connect to database
        # query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'hello': '1'} # Fetches first column that is Employee ID

    def post(self):
        args = parser.parse_args()
        response = chatbot.get_response(args["key"]);
        return 1;

class Tracks(Resource):
    def get(self):
        return {'hello': '1'} # Fetches first column that is Employee ID

class Employees_Name(Resource):
    def get(self, employee_id):
        return {'hello': '1'} # Fetches first column that is Employee ID
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')