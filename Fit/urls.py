from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='inicio'),
    path('calorias', views.calorias , name='calorias'),
    path('usuario', views.usuario , name='usuario'),
    path('crearusuario', views.crearusuario , name='crearusuario'),
    path('deportes',views.deportes ,name='deportes'),
    path('iniciar_sesion', views.iniciar_sesion,name='iniciar_sesion'),
    path('seleccionar',views.seleccionar),
    path('seleccion_deporte',views.seleccion_deporte,name='seleccion_deporte'),
    path('deporte_seleccionado',views.deporte_seleccionado,name='deporte_seleccionado'),
    path('metas',views.metas,name='metas'),
]
