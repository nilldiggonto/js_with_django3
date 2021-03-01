from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(10):
            self.send(json.dumps({'a':randint(0,100)}))
            

            sleep(1)

        # for i in range(10):
        #     self.send(json.dumps({'a':randint(0,100)}))
        #     sleep(1)