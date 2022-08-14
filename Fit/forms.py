from dataclasses import field, fields
from socket import fromshare
from django import forms
from .models import registro

class registroForm(forms.ModelForm):
    class Meta:
       model = registro
       fields = '__all__'

