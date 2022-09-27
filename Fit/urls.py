from django.urls import path, include
from .import views
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.index, name='inicio'),
    path('calorias', views.calorias , name='calorias'),
    path('crearusuario', views.crearusuario , name='crearusuario'),
    path('registration/login', views.iniciar_sesion,name='login'),
    path('perfil/<str:email>', views.usuario , name='usuario'),
    path('calorias', views.calorias , name='calorias'),
    path('Seleccionar_meta',views.Seleccionar_meta,name='Seleccionar_meta'),
    path('ejercicio/<int:email>', views.actividad , name='actividad'),
    path('calendario',views.calendario,name='calendario'),
    path('index',views.index,name='index'),
    

]
