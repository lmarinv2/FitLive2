import re
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,'home.html')

def iniciar_sesion(request):
    return render(request,'iniciar_sesion.html')

def registro_usuario(request):
#    data={
#        'form': registro()
 #   }
#
#    if request.method == 'POST':
#            formulario =Usuario(data=request.POST)
#            if formulario.is_valid():
#                formulario.save()
#                user =authenticate(username=formulario.cleaned_data(["username"]), password=formulario.cleaned_data(["password"]))
#                login(request,user)
    return render(request, 'crear.html')
    #users = Usuario.objects.all()
