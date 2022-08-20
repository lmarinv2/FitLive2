from django.db import models


class registro(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Genero = models.CharField(max_length=40)
    Fecha_nacimiento= models.DateField()
    Email = models.EmailField()
    Peso = models.IntegerField()
    Edad = models.IntegerField()
    Estatura = models.IntegerField()
    Password = models.CharField(max_length=30)


#def __str__(self):
#    fila = " Nombre: " +self.nombre +" " "Apellido: "+ self.apellido
#    return self.fila
