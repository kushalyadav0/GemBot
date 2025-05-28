from pyexpat import model
from django.forms import ModelForm
from .models import *

class InputForm(ModelForm):
    class Meta:
        model = Chat
        fields = "question"