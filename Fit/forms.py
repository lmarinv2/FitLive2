from dataclasses import field, fields
from socket import fromshare
from django import forms
from .models import registro, Deporte

class registroForm(forms.ModelForm):
    class Meta:
       model = registro
       fields = '__all__'

class deportesForm(forms.ModelForm):
    class Meta:
       model = Deporte
       fields = [
            'Deporte',
            'Tiempo',
       ]

