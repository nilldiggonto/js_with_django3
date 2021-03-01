from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'valiue':randint(-20,20)}))
            sleep(1)