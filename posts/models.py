from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Post(models.Model):
    #Connects post to logged-in user.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Stores uploaded photo.
    #Images saved inside:
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
