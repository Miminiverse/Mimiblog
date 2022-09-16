from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=64, null=True)
    text = models.CharField(max_length=100, null = True)
    date_posted = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return f'{self.date_posted} : {self.title}'
