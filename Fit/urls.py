from django.urls import path, include
from .import views
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.home, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crearusuario', views.crearusuario , name='crearusuario'),
    path('registration/login', views.iniciar_sesion,name='login'),
    path('perfil/<str:email>', views.usuario , name='perfil'),
    path('calorias', views.calorias , name='calorias'),
    path('deportes',views.deportes ,name='deportes'),
    path('seleccionar',views.seleccionar),
    path('seleccion_deporte',views.seleccion_deporte,name='seleccion_deporte'),
    path('deporte_seleccionado',views.deporte_seleccionado,name='deporte_seleccionado'),
    path('Seleccionar_meta',views.Seleccionar_meta,name='Seleccionar_meta'),
    path('ejercicio/<int:email>', views.actividad , name='actividad'),
    path('calendario',views.calendario,name='calendario'),
    

]
