from django.urls import path
from .import views

urlpatterns = [
    path('home',views.home, name='inicio'),
    path('calorias', views.calorias , name='calorias'),
    path('usuario', views.usuario , name='usuario'),
    path('crearusuario', views.crearusuario , name='crearusuario'),
    path('deportes',views.deportes ,name='deportes'),
    path('iniciar_sesion', views.iniciar_sesion,name='iniciar_sesion')
]
