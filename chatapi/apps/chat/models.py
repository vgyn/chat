from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    title = models.TextField(max_length=100)
    members = models.ManyToManyField(User)

    class Meta:
        default_related_name = 'chats'


class Message(models.Model):
    text = models.TextField(max_length=1000)
    chat = models.ForeignKey(Chat)
