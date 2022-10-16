from django.urls import path, include
from .import views
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.index, name='inicio'),
    path('crearusuario', views.crearusuario , name='crearusuario'),
    path('registration/login', views.iniciar_sesion,name='login'),
    path('perfil/<str:email>', views.usuario , name='usuario'),
    path('calorias', views.calorias , name='calorias'),
    path('Seleccionar_meta/',views.Seleccionar_meta,name='Seleccionar_meta'),
    path('ejercicio/<int:email>', views.actividad , name='actividad'),
    path('actividad_fisica/<int:email>', views.actividad_fisica , name='actividad_fisica'),
    path('calendario',views.calendario,name='calendario'),
    path('index',views.index,name='index'),
    path('registro_comidas',views.registro_comidas,name='registro_comidas'),
    path('alimentacion',views.alimentacion,name='alimentacion'),
    path('agregar_comida',views.agregar_comida,name='agregar_comida'),
    
    
    

]
