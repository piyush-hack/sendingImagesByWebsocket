import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(websocket, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        websocket.send(text_data=json.dumps({
            'message': message
        }))

