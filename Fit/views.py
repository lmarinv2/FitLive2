import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import registro

from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,'home.html')

def calorias(request):
    return render(request,'calorias.html')

def usuario(request):
    registros = registro.objects.all()
    return render(request, 'usuario.html', {'registros':registros})

def crearusuario(request):
    return render(request, 'crearusuario.html')


