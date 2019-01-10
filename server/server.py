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

class ChatBot(Resource):
    def get(self):
        # conn = db_connect.connect() # connect to database
        # query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'hello': '1'} # Fetches first column that is Employee ID

    def post(self):
        print("here!")
        args = parser.parse_args()
        response = chatbot.get_response(args["key"]);
        return {'response': "{}".format(response)};
        

api.add_resource(ChatBot, '/chatbot') # Route_1

if __name__ == '__main__':
     app.run(port='5002')