import email
from mailbox import NoSuchMailboxError
from pyexpat.errors import messages
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registro, Deporte,Metas
from .forms import registroForm,deportesForm
from django.db.models import F
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from django.contrib.auth.tokens import

# Create your views here.
def home(request):
    return render(request,'home.html')

def crearusuario(request):
    formulario = registroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,"Registado correctamente")
        return redirect('registros')
    return render(request, 'crearusuario.html',{'formulario':formulario})

def iniciar_sesion(request):
    return render(request, 'registration/login.html')

def usuario(request,email):
    direcciones=registro.objects.filter(Email__icontains=email)
    calorias(request)
    return render(request, "usuario.html",{"registros":direcciones})

def calorias(request):
    registros = registro.objects.all()
    sexo = registro.objects.values_list('Genero','Edad','Peso','Email')
    sexo = [list(elem) for elem in sexo]
    edad = registro.objects.values_list('Edad')
    edad = [list(elem) for elem in edad]
    peso = registro.objects.values_list('Peso')
    peso = [list(elem) for elem in peso]
    email = registro.objects.values_list('Email')

    a = 0;
    for i in peso:         
        b = 0;
        for j in i :
            d = 0;
            if sexo[a][b] == 'Femenino':
                b = b+1;

                if sexo[a][1] <= 18:
                    caloria = 13.384 * sexo[a][2]  + 692.6;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
                    
                if sexo[a][1] > 18 and sexo[a][1] <= 30:
                    caloria = 14.818 * sexo[a][2]  + 486.6;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
                
                if sexo[a][1] > 30 and sexo[a][1] <=60:
                    caloria = 8.126 * sexo[a][2]  + 845.6;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
                
                if sexo[a][1] > 60:
                    caloria = 9.082 * sexo[a][2]  + 658.5;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)

            else:
                if sexo[a][1] <= 18:                                             
                    caloria = 17.686 * sexo[a][2]  + 658.2;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
                
                if sexo[a][1] > 18 and sexo[a][1] <= 30:
                    caloria = 15.057 * sexo[a][2]  + 692.2;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
                
                if sexo[a][1] > 30 and sexo[a][1] <=60:
                    caloria = 11.472 * sexo[a][2]  + 873.1;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
                
                if sexo[a][1] > 60:
                    caloria = 11.711 * sexo[a][2]  + 587.7;
                    registro.objects.filter(Email=sexo[a][3]).update(calorias=caloria)
        a = a+1;

def actividad(request,email):
    form = deportesForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            dep = request.POST.get("Deporte")
            tiem = request.POST.get("Tiempo")
            usuario = registro.objects.filter(pk=email).values_list('Peso')
            usuario = [list(elem) for elem in usuario]
            print(dep)
            print(usuario[0][0])
            if dep == "ci":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        print("entro")
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 230 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 280 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 330 )
                        b.save()
                
                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        print("entro")
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 460 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 560 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 660 )
                        b.save()

            elif dep == "na":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        print("entro")
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 180 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 216 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 252 )
                        b.save()

                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        print("entro")
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 360 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 432 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 504 )
                        b.save()
            
            elif dep == "cr":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 180 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 216 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 252 )
                        b.save()

                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 360 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 432 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 504 )
                        b.save()
            
            elif dep == "gi":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 90 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 108 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 126 )
                        b.save()
                
                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 180 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 216 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 252 )
                        b.save()    

            elif dep == "co":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 135 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 175 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 189 )
                        b.save()
                
                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 270 )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 350 )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=email), Deporte=dep, Tiempo= tiem, calorias_deporte = 378 )
                        b.save()
            else:
                pass

    return render(request, "actividad_fisica.html",{"formulario":form})
    
def deportes(request):
    return render(request, 'deportes.html')
    registros = registro.objects.all()
    id = registro.objects.values_list('id')
    id = [list(elem) for elem in id]
    deportes={'1':"Ciclismo",
            '2':"Natación",
            '3':"Correr",
            '4':"Gimnasio",
            '5':"Crossfit", 
            }
    for i in range(len(id)):
        
        eleccion = int(input(
            "Ingrese el numero correspondiente al deporte a practicar:\n(1)->Ciclismo\n(2)->Natacion\n(3)->Correr\n("
            "4)->Gimnasio\n(5)->Crossfit"))
        if eleccion == 1:
            print(f' Has seleccionado ciclismo')
            print('Este deporte quema 290  y 384 calorias por sesion')
            registros[i]['deporte']='ciclismo'
        elif eleccion == 2:
            print('Has seleccionado Natacion')
            print('Este deporte quema entre 180 y 250 calorias por sesion')
            registros[i]['deporte'] = 'Natacion'
        elif eleccion == 3:
            print('Has seleccionado Correr')
            print('Este deporte quema entre 240 y 336 calorias por sesion')
            registros[i]['deporte'] = 'Correr'
        elif eleccion == 4:
            print('Has seleccionado Gimnasio')
            print('Este deporte quema entre 250 y 295 calorias por sesion')
            registros[i]['deporte'] = 'Gimnasio'
        elif eleccion == 5:
            print('Has seleccionado Crossfit')
            print('Este deporte quema entre 261 y 289 calorias por sesion')
            registros[i]['deporte'] = 'Crossfit'
        elif eleccion < 1 or eleccion > 5:
            print("Error")

def seleccionar(request):
    
    if request.GET["Email"]:
        print(request.GET["Email"])
        mensaje="Bienvenido : %r" %request.GET["Email"]
        correo=request.GET["Email"]
        
        direcciones=registro.objects.filter(Email__icontains=correo)
        return render(request, "seleccion_deporte.html",{"direcciones":direcciones,"query":correo})
    else:
        mensaje="No has introducido ningun Email"
        
    return HttpResponse(mensaje)

def seleccion_deporte(request):
    return render(request,"seleccion_deporte")

def deporte_seleccionado(request):
    resultado=request.GET["opciones_deporte"]
    return render(request,"deporte_seleccionado.html",{"opciones_deporte":resultado})

def Seleccionar_meta(request):
    if request.method=='POST':
        print(request)
        if request.POST.get('Seleccionar_meta'):
            savemeta=Metas()
            savemeta.eleccion=request.POST.get('Seleccionar_meta')
            savemeta.save()
            messages.success(request, "Meta seleccionada correctamente")
            
            
    return render(request,"Seleccionar_meta.html")



def calendario(request):
    return render(request,'calendario.html')


    