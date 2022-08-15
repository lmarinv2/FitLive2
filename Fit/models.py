from django.db import models


class registro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sexo = models.CharField(max_length=40)
    fecha_nacimiento= models.DateField()
    email = models.EmailField()
    peso = models.IntegerField()
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=40)

class calorias(models.Model):
    kal = models.IntegerField()

#def __str__(self):
#    fila = " Nombre: " +self.nombre +" " "Apellido: "+ self.apellido
#    return self.fila
