from django.db import models

from .choices import deportes

class registro(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Genero = models.CharField(max_length=40)
    Fecha_nacimiento= models.DateField()
    Email = models.EmailField()
    Peso = models.IntegerField()
    Edad = models.IntegerField()
    Estatura = models.IntegerField()
    calorias = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):
#fila = " Nombre: " +self.nombre +" " "Apellido: "+ self.apellido
       return self.Email


class Deportes(models.Model):
    Deporte=models.CharField(max_length=20,choices=deportes)
    Tiempo=models.IntegerField()
    calorias = models.CharField(max_length=30,null=True,blank=True)
    usuario=models.ForeignKey(registro,null=True,blank=True,on_delete=models.CASCADE)