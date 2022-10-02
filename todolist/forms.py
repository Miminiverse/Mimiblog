from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
<<<<<<< HEAD
        fields = '__all__'
        
=======
        fields = '__all__'
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
