from distutils.log import debug
from flask import Flask
from flask_restful import Api

# Dev Web Server Definitions and Initialization Class
class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app)
    
    def run(self, ):
        self.app.run(
            debug=True
        )
        
server = Server()