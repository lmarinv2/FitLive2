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
    Password = models.CharField(max_length=30)


    def __str__(self):
#fila = " Nombre: " +self.nombre +" " "Apellido: "+ self.apellido
       return self.Email


class Deportes(models.Model):
    Deporte=models.CharField(max_length=20,choices=deportes)
    usuario=models.ForeignKey(registro,null=True,blank=True,on_delete=models.CASCADE)