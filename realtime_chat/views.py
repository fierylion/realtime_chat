from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatRoom, ChatMessage
from .serializers import ChatMessageSerializer, ChatRoomSerializer
from rest_framework import viewsets
from utils.paginations import StandardResultsSetPagination
from utils.filter_backend import default_filter_backends


# Create your views here.
class ChatViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def create(self, request):
        data = request.data
        chat = ChatRoomSerializer(data=data)
        if chat.is_valid():
            chat.save()
            return Response(chat.data, status=status.HTTP_201_CREATED)
        else:
            return Response(chat.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = ChatMessageSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = default_filter_backends
    filterset_fields = ['room', 'creator']

    def get_queryset(self):
        return ChatMessage.objects.all().order_by('created_at')

    def list(self, request, *args, **kwargs):
        room = request.query_params.get('room')
        if room is not None:
            try:
                ChatRoom.objects.get(id=room)
            except ChatRoom.DoesNotExist:
                return Response({
                    "count": 0,
                    "next": None,
                    "previous": None,
                    "results": [],
                }, status=status.HTTP_200_OK)
        return super().list(request, *args, **kwargs)
