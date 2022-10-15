from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    last_name = models.TextField()
    location = models.CharField(max_length=100, blank =True)
    age = models.IntegerField()
    bio = models.TextField(blank = True)

    def __str__(self):
        return self.User.username