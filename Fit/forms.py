from dataclasses import field, fields
from socket import fromshare
from django import forms
from .models import registro 
from .choices import deportes, tiempo

class registroForm(forms.ModelForm):
    class Meta:
       model = registro
       exclude = ['calorias']

class deportesForm(forms.Form):
    Deporte = forms.TypedChoiceField(
        widget=forms.Select(choices=deportes)
    )
    Tiempo = forms.IntegerField(
        widget=forms.Select(choices=tiempo)
    )
    Fecha = forms.DateField()

