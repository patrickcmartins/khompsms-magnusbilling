from datetime import datetime
from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from json import dumps
from asterisk.ami import AMIClient
import requests
import logging

app = Flask(__name__)
api = Api(app)

class SMS(Resource):
    client = AMIClient(address='127.0.0.1',port=5038)
    def get(self, numero, mensagem):
        
    
    
