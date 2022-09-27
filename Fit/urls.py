from django.urls import path, include
from .import views
from django.contrib.auth.models import User

urlpatterns = [
<<<<<<< HEAD
    path('',views.home, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
=======
    path('',views.index, name='inicio'),
    path('calorias', views.calorias , name='calorias'),
    path('usuario/<str:email>', views.usuario , name='usuario'),
>>>>>>> 74bd0a3c9c7b287f667a9ed23d29b62a58228d31
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
    path('index',views.index,name='index'),
    

]
