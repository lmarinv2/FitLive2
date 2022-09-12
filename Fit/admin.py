from django.contrib import admin

from Fit.models import Deporte, registro, Metas


# Register your models here.
#
#admin.site.register(registro)
#admin.site.register(Deporte)

@admin.register(registro)
class registroAdmin(admin.ModelAdmin):
    list_display=('id','Nombre','Apellido','Email')

@admin.register(Deporte)
class DeportesAdmin(admin.ModelAdmin):
    list_display=('Deporte','usuario')    

@admin.register(Metas)
class MetasAdmin(admin.ModelAdmin):
    list_display=('usuario', 'Descripcion','Dificultad','Puntos')
    