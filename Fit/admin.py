from django.contrib import admin

from Fit.models import Deportes, registro


# Register your models here.

#admin.site.register(registro)
#admin.site.register(Deportes)

@admin.register(registro)
class registroAdmin(admin.ModelAdmin):
    list_display=('id','Nombre','Apellido','Email')


@admin.register(Deportes)
class DeportesAdmin(admin.ModelAdmin):
    list_display=('Deporte','usuario')

    