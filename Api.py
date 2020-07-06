from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Main(Resource):
  
  def post(self):
      return f"It works!", 201
      
api.add_resource(Main, '/')

if __name__ == '__main__':
  app.run(debug=True, port=443)