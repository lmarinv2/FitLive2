import email
from mailbox import NoSuchMailboxError
from pyexpat.errors import messages
import re
from xml.dom.minidom import Identified
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bedidas, Comida, registro, Deporte,Metas
from .forms import comidaForm, registroForm,deportesForm
from django.db.models import F
from django.contrib import messages
from django.contrib.auth import authenticate, login
from datetime import date, datetime
from datetime import datetime
import datetime
import pandas as pd

emailperfil = "lauramarin452@gmail.com"
idperfil = "7"

#from django.contrib.auth.tokens import
# Create your views here.

#def iniciar_sesion(request):
#    return render(request, 'registration/login.html')
#################################################################################################################################
def home(request):
    email = request.POST.get("email")
    global emailperfil
    emailperfil = email
    global idperfil
    sexo = registro.objects.values_list('pk','Email')
    sexo = [list(elem) for elem in sexo]
    a = 0;
    for i in sexo:         
        b = 0;
        for j in i :
            d = 0;
            if sexo[a][1] == emailperfil:
                b = b+1;
                idperfil = sexo[a][0]
        a = a+1;
    return render(request,'home.html')
###########################################################################################################################
def index(request):
    return render(request,'index.html')
##########################################################################################################################
def crearusuario(request):
    formulario = registroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,"Registado correctamente")
        return redirect('registros')
    return render(request, 'crearusuario.html',{'formulario':formulario})
###########################################################################################################################
def usuario(request,):
    direcciones=registro.objects.filter(Email__icontains=emailperfil)
    calorias()
    return render(request, "usuario.html",{"registros":direcciones})
###########################################################################################################################
def calorias():
    sexo = registro.objects.values_list('Genero','Edad','Peso','Email')
    sexo = [list(elem) for elem in sexo]
    edad = registro.objects.values_list('Edad')
    edad = [list(elem) for elem in edad]
    peso = registro.objects.values_list('Peso')
    peso = [list(elem) for elem in peso]
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
###########################################################################################################################
def actividad(request):
    print(request.POST.get("Fecha"))
    if request.method == "POST":
            dep = request.POST.get("Deporte")
            tiem = request.POST.get("Tiempo")
            fech = request.POST.get("Fecha")
            usuario = registro.objects.filter(pk=idperfil).values_list('Peso')
            usuario = [list(elem) for elem in usuario]
            if dep == "ci":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 230, Fecha =fech)
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 280, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 330, Fecha =fech )
                        b.save()
                
                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 460, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 560, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 660, Fecha =fech )
                        b.save()

            elif dep == "na":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 180, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 216, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 252, Fecha =fech )
                        b.save()

                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 360, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 432, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 504, Fecha =fech )
                        b.save()
            
            elif dep == "cr":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 180, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 216, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 252, Fecha =fech )
                        b.save()

                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 360, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 432, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 504, Fecha =fech )
                        b.save()
            
            elif dep == "gi":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 90, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 108, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 126, Fecha =fech )
                        b.save()
                
                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 180, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 216, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 252, Fecha =fech )
                        b.save()    

            elif dep == "co":
                if tiem == "30":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 135, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 175, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 189, Fecha =fech )
                        b.save()
                
                elif tiem == "100":
                    if usuario[0][0] <= 65: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 270, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 66 and usuario[0][0] <= 75: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 350, Fecha =fech )
                        b.save()
                    elif usuario[0][0] >= 76: 
                        b = Deporte(usuario=registro(pk=idperfil), Deporte=dep, Tiempo= tiem, calorias_deporte = 378, Fecha =fech )
                        b.save()
            else:
                pass
            messages.success(request, "Deporte añadido correctamente")

    return render(request, "actividad_fisica.html")
###########################################################################################################################
def agregar_bebidas(request):
    if request.method == "POST":
            beb = request.POST.get("Bebida")
            cant = request.POST.get("Cantidad")
            fech = request.POST.get("Fecha")
            if beb == "Agua":
                        b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 0, Fecha =fech)
                        b.save()
            elif beb == "Jugo":
                if cant == "250":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 137, Fecha =fech )
                    b.save()
                elif cant == "500":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 275, Fecha =fech )
                    b.save()
                elif cant == "1000":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 550, Fecha =fech )
                    b.save()

            elif beb == "Gaseosa":
                if cant == "250":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 102, Fecha =fech )
                    b.save()
                elif cant == "500":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 205, Fecha =fech )
                    b.save()
                elif cant == "1000":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 410, Fecha =fech )
                    b.save()

            elif beb == "Infusion":
                if cant == "250":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 2, Fecha =fech )
                    b.save()
                elif cant == "500":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 4, Fecha =fech )
                    b.save()
                elif cant == "1000":
                    b = Bedidas(usuario=registro(pk=idperfil), Bebida=beb, Cantidad= cant, calorias_Bedida = 6, Fecha =fech )
                    b.save()
            else:
                pass
            messages.success(request, "Bebida añadida")
    return render(request,'agregar_bebidas.html')
###########################################################################################################################
def Seleccionar_meta(request):
    if request.method=='POST':
        print(request)
        if request.POST.get('Seleccionar_meta'):
            savemeta=Metas()
            savemeta.eleccion=request.POST.get('Seleccionar_meta')
            savemeta.save()
            messages.success(request, "Meta seleccionada correctamente")       
    return render(request,"Seleccionar_meta.html")
###########################################################################################################################
def alimentacion(request):
    return render(request,'alimentacion.html')
###########################################################################################################################
def calendario(request):
    return render(request,'calendario.html')
###########################################################################################################################
def estadisticas(request):
    if request.method == "POST":
        fechinc = request.POST.get("Fechainicio")
        fechfin = request.POST.get("Fechafinal")
        start = datetime.datetime.strptime(fechinc, "%Y-%m-%d")
        end = datetime.datetime.strptime(fechfin, "%Y-%m-%d")
        date_generated = pd.date_range(start, end)
        usuario = registro.objects.filter(pk=idperfil).values_list('pk')
        usuario = [list(elem) for elem in usuario]
        beb = Bedidas.objects.values_list('Bebida','Fecha','calorias_Bedida','usuario')
        beb = [list(elem) for elem in beb]
        Dep = Deporte.objects.values_list('Deporte','Tiempo','Fecha','calorias_deporte','usuario')
        Dep = [list(elem) for elem in Dep]


        calorias_consumidas = 0
        contador1=0;
        b = 0;
        for j in beb:
            a=0
            for i in date_generated:    
                if beb[b][3] == int(idperfil):   
                    if date_generated[a] == pd.Timestamp(beb[b][1]):
                        calorias_consumidas= calorias_consumidas + int(beb[b][2])
                        contador1=contador1+1;
                a=a+1
            b=b+1
        ########################################################################################3
        calorias_gastadas = 0
        contador2=0;
        c=0
        for j in Dep:
            d=0
            for i in date_generated: 
                if Dep[c][4] == int(idperfil):   
                    if date_generated[d] == pd.Timestamp(Dep[c][2]):
                        calorias_gastadas= calorias_gastadas + int(Dep[c][3])
                        contador2=contador2+1;
                d=d+1
            c=c+1

        promedio_consumidas = calorias_consumidas/contador1
        promedio_gastadas = calorias_gastadas/contador2

        print(promedio_consumidas)
        print(promedio_gastadas)
        
    return render(request,'estadisticas.html', {'consumidas':promedio_consumidas , 'gastadas':promedio_gastadas})
###########################################################################################################################
def registro_comidas(request):
    return render(request,'registro_comidas.html')
    print(datetime.today())
###########################################################################################################################
def agregar_comida(request):
    return render(request,'agregar_comida.html')
###########################################################################################################################
def agregar_comidas(request):
    if request.method=='POST':
        form=comidaForm(request.POST)
       
        form.save()
        return redirect('registro_comidas')
    else:
        form=comidaForm()
        
    return render(request,'agregar_comida.html',{'form':form})
###########################################################################################################################
def agregar_comida(request):
    if request.method == "POST":
        com = request.POST.get("Comida")
        car = request.POST.get("Carbohidratos")
        pro = request.POST.get("Proteina")
        gra = request.POST.get("Grasas")
        if (com == "Desayuno")or(com == "Almuerzo")or(com == "Cena")or(com == "Snacks"):
            totalcalorias=0
            if car=="0":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Carbohidratos=car, calorias_Comida=0)
                c.save()
            elif car=="25":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Carbohidratos=car, calorias_Comida=100)
                c.save()
            elif car=="25":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Carbohidratos=car, calorias_Comida=100)
                c.save()
            elif car=="25":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Carbohidratos=car, calorias_Comida=100)
                c.save()
            elif car=="25":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Carbohidratos=car, calorias_Comida=100)
                c.save()
                
            if pro=="0":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=0)
                c.save()
            elif pro=="25":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=100)
                c.save()
            elif pro=="50":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=200)
                c.save()
            elif pro=="100":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=400)
                c.save()
            elif pro=="150":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=600)
                c.save()
            elif pro=="250":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=1000)
                c.save()
            elif pro=="350":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Proteina=car, calorias_Comida=1400)
                c.save()

            if gra=="0":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Grasas=gra, calorias_Comida=0)
                c.save()
            elif gra=="10":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Grasas=gra, calorias_Comida=90)
                c.save()
            elif gra=="20":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Grasas=gra, calorias_Comida=180)
                c.save()
            elif gra=="40":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Grasas=gra, calorias_Comida=360)
                c.save()
            elif gra=="60":
                c=Comida(usuario=registro(pk=idperfil), Comida=com,Grasas=gra, calorias_Comida=540)
                c.save()
            else:
                pass
            messages.success(request, "Comida añadida")
    return render(request,'agregar_comida.html')
