from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='inicio'),
    path('calorias', views.calorias , name='calorias'),
    path('usuario', views.usuario , name='usuario'),
    path('crearusuario', views.crearusuario , name='crearusuario'),
]
