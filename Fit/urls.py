from django.urls import path, include
from .import views
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.index, name='inicio'),
    path('crearusuario', views.crearusuario , name='crearusuario'),
    path('registration/login', views.iniciar_sesion,name='login'),
    path('perfil/<str:email>', views.usuario , name='usuario'),
    path('Seleccionar_meta/',views.Seleccionar_meta,name='Seleccionar_meta'),
    path('ejercicio/<int:email>', views.actividad , name='actividad'),
    path('actividad_fisica/<int:email>', views.actividad_fisica , name='actividad_fisica'),
    path('calendario',views.calendario,name='calendario'),
    path('index',views.index,name='index'),
    path('registro_comidas',views.registro_comidas,name='registro_comidas'),
    path('agregar_bebidas/<int:email>',views.agregar_bebidas,name='agregar_bebidas'),
    path('registro_bebidas',views.registro_bebidas,name='registro_bebidas'),
    path('alimentacion',views.alimentacion,name='alimentacion'),
    path('agregar_comida',views.agregar_comida,name='agregar_comida'),
    
    
    

]
