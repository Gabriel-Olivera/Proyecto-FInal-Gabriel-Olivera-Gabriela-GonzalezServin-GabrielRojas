from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # username=models.CharField(User.username, max_length=255, default='admin')
    content=models.CharField(max_length=255)
    timestamp=models.DateTimeField(auto_now=True)
    destinatario=models.CharField(max_length=255)
    
    def __str__(self):
        return self.user+" | "+self.destinatario+" | "+str(self.timestamp)

class messagesChat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    username=User.username
    content=models.CharField(max_length=255)
    timestamp=models.DateTimeField(auto_now=True)
    destinatario=models.CharField(max_length=255)
    
    def __str__(self):
        return self.user+" | "+self.destinatario+" | "+str(self.timestamp)
