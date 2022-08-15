from mailbox import NoSuchMailboxError
import re
from django.shortcuts import render
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
    sexo = registro.objects.values_list('sexo','estatura','peso')
    sexo = [list(elem) for elem in sexo]
    edad = registro.objects.values_list('estatura')
    edad = [list(elem) for elem in edad]
    peso = registro.objects.values_list('peso')
    peso = [list(elem) for elem in peso]

    #.annotate(resta=F('estatura') - F('peso'))
    #print(sexo);
    #print(sexo[2][0]);
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
                    caloria = 13.384 * sexo[a][2]  + 692.6;
                    print (caloria);
                
                if sexo[a][1] > 18 and sexo[a][1] <= 30:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 14.818 * sexo[a][2]  + 486.6;
                    print (caloria);
                
                if sexo[a][1] > 30 and sexo[a][1] <=60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 8.126 * sexo[a][2]  + 845.6;
                    print (caloria);
                
                if sexo[a][1] > 60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 9.082 * sexo[a][2]  + 658.5;
                    print (caloria);


            else:
                if sexo[a][1] <= 18:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");                                                   
                    caloria = 17.686 * sexo[a][2]  + 658.2;
                    print (caloria);
                
                if sexo[a][1] > 18 and sexo[a][1] <= 30:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 15.057 * sexo[a][2]  + 692.2;
                    print (caloria);
                
                if sexo[a][1] > 30 and sexo[a][1] <=60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 11.472 * sexo[a][2]  + 873.1;
                    print (caloria);
                
                if sexo[a][1] > 60:
                    print("sexo: ");
                    print(sexo[a][0]);
                    print("edad: ");
                    print(sexo[a][1]);
                    print("calorias reposo");
                    caloria = 11.711 * sexo[a][2]  + 587.7;
                    print (caloria);


        a=a+1;
 
 #              # caloria = registro.objects.values('email').annotate(caloria=F('estatura') - F('peso'))
 #              caloria = 13.384 *F('peso')  + 692.6
 #              print (caloria);
 #           elif registro.estatura > 18 & registro.estatura <= 30:
 #              caloria = 14.818 * registro.peso + 486.6
 #           elif registro.estatura > 30 & registro.estatura <=60:
 #              caloria = 8.126 * registro.peso + 845.6
 #           elif registro.estatura > 60:
 #              caloria = 9.082 * registro.peso + 658.5
            
                                                                               #la variable estatura es la edad
   #     if sexo == "Masculino":
   #         if edad <= 18:
   #             caloria = 17.686* peso + 658.2
   #         elif edad > 18 & edad <= 30:
   #             caloria = 15.057* peso + 692.2
   #         elif edad > 30 & edad <=60:
   #             caloria = 11.472 * peso + 873.1
   #         elif edad > 60:
   #             caloria = 11.711 * peso + 587.7
   #  
    return render(request,'calorias.html',{'registros':registros})

def usuario(request):
    registros = registro.objects.all()
    return render(request, 'usuario.html', {'registros':registros})

def crearusuario(request):
    formulario = registroForm(request.POST or None)
    return render(request, 'crearusuario.html',{formulario:formulario})

def deportes(request):
    return render(request, 'deportes.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')


