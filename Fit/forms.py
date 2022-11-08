from dataclasses import field, fields
from re import A
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import registro, Comida
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
    
class comidaForm(forms.ModelForm):
     class Meta:
         model=Comida
         fields=[
            'Comida',
            'Carbohidratos',
            'Proteina',
            'Grasas',
        
            ]
         
         labels={
            'Comida':'Comida',
            'Carbohidratos':'Carbohidratos',
            'Proteina':'Proteina',
            'Grasas':'Grasas',
        }
         widgets={
            'Comida':forms.CheckboxSelectMultiple(),
            'Carbohidratos':forms.Select(attrs={'class':'form-control'}),
            'Proteina':forms.Select(attrs={'class':'form-control'}),
            'Grasas':forms.Select(attrs={'class':'form-control'}),
            
            
        }
    
        
    

