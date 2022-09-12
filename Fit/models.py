from django.db import models

from .choices import deportes,metas,puntos


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
       return self.Email


class Deporte(models.Model):
    Deporte=models.CharField(max_length=20,choices=deportes)
    Tiempo=models.IntegerField(null=True,blank=True)
    calorias_deporte = models.CharField(max_length=30,null=True,blank=True)
    usuario=models.ForeignKey(registro,null=True,blank=True,on_delete=models.CASCADE)
    
    
class Metas(models.Model):
    eleccion=models.IntegerField(null=True,blank=True)
    Dificultad=models.CharField(max_length=20,choices=metas)
    Descripcion=models.TextField(max_length=100)
    Puntos=models.CharField(max_length=20,choices=puntos)
    usuario=models.ForeignKey(registro,null=True,blank=True,on_delete=models.CASCADE)
    
    