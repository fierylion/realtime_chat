from rest_framework import serializers
from .models import ChatRoom, ChatMessage, ExpertUser


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ExpertUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertUser
        fields=['id', 'expert_id', 'username', 'created_at']
        read_only_fields = ['created_at', 'id']
        


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'room', 'creator', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
