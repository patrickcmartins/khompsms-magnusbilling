from msilib.schema import Class
from pyami_asterisk import AMICLient
import random

class ASTAMI():
    ami = AMIClient(host='127.0.0.1', port=5038, username='username', secret='password')
    
    def callback_originate(events):
        print(events)

    def sendSMS(self, numero, mensagem):
        self.ami.create_action(
            {
                "Action": "KSendSMS",
                "Device": "B0C" + str(random.randint(0,10)),
                "Destination": numero,
                "Message": mensagem,
            },
        self.callback_originate,
        )
        self.ami.connect()
