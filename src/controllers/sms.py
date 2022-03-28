from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from asterisk.ami import AMIClient, SimpleAction
import random
import time

from src.server.instance import server 

app, api = server.app, server.api

#Define asterisk host and port to connect ami client
client = AMIClient(address='127.0.0.1',port=5038)

class SendSMS(Resource):
    def get(self, ):
        numero = request.args.get("numero")
        mensagem = request.args.get("mensagem")
        
        #Change username and password to your own created in /etc/asterisk/manager.conf
        client.login(username='magnus',secret='magnussolution')
        
        #Define the Send SMS action thru simple action
        action = SimpleAction(
            'KSendSMS',
            #Change the 10 for your total number of channels, if you have 15 sim cards just put (0,15)
            Device='B0C'+ str(random.randint(0,10)),
            Destination= numero,
            Message=mensagem
        )
        
        #Execute the action
        future = client.send_action(action)
        
        #Sleep 0.5s to get the output generated from asterisk ami
        time.sleep(0.5)    
        # client.logoff()
        
        #Get the response 
        response = str(future.response)
        
        #If loop to nofify magnus if the request went successful or not
        if response.startswith("Response: Error"):
            response = 'false'
        else:
            response = 'true' 
        
        return response, 200
    
api.add_resource(SendSMS, '/sendsms')