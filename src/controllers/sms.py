from flask import Flask, jsonify, request
from flask_restful import Api, Resource
# from asterisk.ami import AMIClient, SimpleAction
from src.controllers.astfunc import ASTAMI

from src.server.instance import server 

app, api = server.app, server.api



class SendSMS(Resource):
    def get(self, ):
        numero = request.args.get("numero")
        mensagem = request.args.get("mensagem")
        
        astami = ASTAMI()
        
        event = astami.sendSMS(numero, mensagem)
        
        if response.startswith("Response: Error"):
            response = 'false'
        else:
            response = 'true'     
        
        return response, 200
    
api.add_resource(SendSMS, '/sendsms')