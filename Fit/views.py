from mailbox import NoSuchMailboxError
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registro
from .forms import registroForm
from django.db.models import F

from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,'home.html')

def calorias(request):
    registros = registro.objects.all()
    sexo = registro.objects.values_list('sexo','edad','peso')
    sexo = [list(elem) for elem in sexo]
    edad = registro.objects.values_list('edad')
    edad = [list(elem) for elem in edad]
    peso = registro.objects.values_list('peso')
    peso = [list(elem) for elem in peso]

    caloria1=0;

    kal =[];
    a =0;
    for i in peso:        
        b=0;
        for j in i :
            if sexo[a][b] == 'Femenino':
                b=b+1;

                if sexo[a][1] <= 18:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria1 = 13.384 * sexo[a][2]  + 692.6;
                    print (caloria1);
                    kal.append(int(caloria1))
                
                if sexo[a][1] > 18 and sexo[a][1] <= 30:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 14.818 * sexo[a][2]  + 486.6;
                    print (caloria);
                    kal.append(int(caloria))
                
                if sexo[a][1] > 30 and sexo[a][1] <=60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 8.126 * sexo[a][2]  + 845.6;
                    print (caloria);
                    kal.append(int(caloria))
                
                if sexo[a][1] > 60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 9.082 * sexo[a][2]  + 658.5;
                    print (caloria);
                    kal.append(int(caloria))


            else:
                if sexo[a][1] <= 18:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");                                                   
                    caloria = 17.686 * sexo[a][2]  + 658.2;
                    print (caloria);
                    kal.append(int(caloria))
                
                if sexo[a][1] > 18 and sexo[a][1] <= 30:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 15.057 * sexo[a][2]  + 692.2;
                    print (caloria);
                    kal.append(int(caloria))
                
                if sexo[a][1] > 30 and sexo[a][1] <=60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 11.472 * sexo[a][2]  + 873.1;
                    print (caloria);
                    kal.append(int(caloria))
                
                if sexo[a][1] > 60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 11.711 * sexo[a][2]  + 587.7;
                    print (caloria);
                    kal.append(int(caloria))


        a=a+1;
    print (kal);
    kalo=[];
    c=0;
    for i in range(6):
        kalo.append([]);
        for j in range(1):
            kalo[c].append(kal[i]);
            c+=1;
    print(kalo)

    return render(request,'calorias.html',{'c':kalo})

def usuariocal(request):
    registros = registro.objects.all()
    return render(request, 'calorias.html', {'registros':registros})

def usuario(request):
    registros = registro.objects.all()
    return render(request, 'usuario.html', {'registros':registros})

def crearusuario(request):
    formulario = registroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registros');
    return render(request, 'crearusuario.html',{'formulario':formulario})

def deportes(request):
    return render(request, 'deportes.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')