import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class RoomConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        room_created = await self.create_room(self.room_name)
        if room_created[1]:
            await self.accept()
        else:
            await self.send(text_data=json.dumps({
                'error': room_created[0]
            }))
            await self.close()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        print(text_data_json)

        result = await self.save_message(text_data_json, self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'room_message',
                'result': result,
                'sender_channel_name': self.channel_name
            }
        )

    async def room_message(self, event):
        (message, no_error) = event['result']
        if no_error and event['sender_channel_name'] != self.channel_name:
            await self.send(text_data=json.dumps({
                'message': message
            }))
        if not no_error and event['sender_channel_name'] == self.channel_name:
            await self.send(text_data=json.dumps({
                'error': message
            }))
    

    @sync_to_async
    def create_room(self, room_name):
        from .serializers import ChatRoomSerializer
        serializer = ChatRoomSerializer(data={'id': room_name})
        if serializer.is_valid():
            serializer.save()
            return serializer.data, True
        elif "exist" in serializer.errors['id'][0]:
            return "already exist", True
        else:
            return serializer.errors, False

    @sync_to_async
    def save_message(self, text_data, room):
        from .serializers import ChatMessageSerializer
        from .serializers import ExpertUserSerializer
        from .models import ExpertUser
        expert_id = room.split('_')[1]
        user_id = room.split('_')[0]
        
        if text_data['creator'] == 'user':
            username= text_data["username"]
            expert_user = ExpertUser.objects.filter(id=room).exists()
            if not expert_user:
                expert_user = ExpertUserSerializer(data={"id":room,'expert_id': expert_id, 'username': username , 'user_id': user_id})
                if expert_user.is_valid():
                    expert_user.save()
                else:
                
                    return expert_user.errors, False


        text_data['room'] = room
   
        chat = ChatMessageSerializer(data=text_data)
        if chat.is_valid():
            chat.save()
            print(chat.data)
            return chat.data, True
        else:
        
            return chat.errors, False
