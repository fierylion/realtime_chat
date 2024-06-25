from django.db import models
from utils.models import CuidField


# Create your models here.

class ChatRoom(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class ChatMessage(models.Model):
    CREATOR_CHOICES = (
        ('user', 'heslb'),
        ('heslb', 'heslb'),
    )
    id = CuidField(primary_key=True, prefix='message_')
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    creator = models.CharField(max_length=50, choices=CREATOR_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
