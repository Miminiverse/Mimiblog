
from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.template.defaultfilters import slugify
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_1.jpg', upload_to='profile_pics')
=======

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c

    def __str__(self):
        return f'{self.user.username} Profile'





