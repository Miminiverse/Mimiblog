from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=64, null=True)
    text = models.TextField(max_length=1000, null = True)
    audio = models.FileField(upload_to = 'audio_files', null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return f'{self.date_posted} : {self.title}'
    
    def get_absolute_url(self):
        return reverse ('post-detail', kwargs={'pk': self.pk})

    
