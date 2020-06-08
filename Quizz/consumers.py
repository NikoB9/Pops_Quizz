# Quizz/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        type = text_data_json['type']
        user = text_data_json['user']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type,
                'user': user,
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type' : 'chat_message',
            'user': user,
            'message': message
        }))

    # Annoncer l'arrivé d'un membre
    async def connect_on(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'connect_on',
            'user': user,
            'message': message
        }))

class WaitingRoom(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['idgame']
        self.room_group_name = 'waiting_room_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        type = text_data_json['type']
        user = text_data_json['user']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type,
                'user': user,
                'message': message
            }
        )

    # Annoncer l'arrivé d'un membre
    async def connect_on(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'connect_on',
            'user': user,
            'message': message
        }))

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'user': user,
            'message': message
        }))

    # Receive message from room group
    async def refresh(self, event):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'refresh',
        }))