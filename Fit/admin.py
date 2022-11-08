from django.contrib import admin

from Fit.models import Bedidas, Deporte, registro, Metas,Comida


# Register your models here.
#
#admin.site.register(Bedidas)
#admin.site.register(Deporte)

@admin.register(registro)
class registroAdmin(admin.ModelAdmin):
    list_display=('Email','Nombre','Apellido')

@admin.register(Deporte)
class DeportesAdmin(admin.ModelAdmin):
    list_display=('usuario','Deporte')    

@admin.register(Metas)
class MetasAdmin(admin.ModelAdmin):
    list_display=('usuario', 'Descripcion','Dificultad','Puntos')

@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display=('Comida','usuario')  

@admin.register(Bedidas)
class registroAdmin(admin.ModelAdmin):
    list_display=('usuario','Bebida')
    

    