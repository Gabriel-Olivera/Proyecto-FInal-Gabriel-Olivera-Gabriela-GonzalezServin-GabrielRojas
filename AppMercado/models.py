from django.db import models

# Create your models here.

class Electrodomesticos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50,)
    precio = models.IntegerField()
    email_contacto = models.EmailField()
    fecha_publicacion = models.DateField()

class Muebles(models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length=50) 
    precio = models.IntegerField()
    email_contacto = models.EmailField()
    fecha_publicacion = models.DateField()

class Vehiculos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    email_contacto = models.EmailField()
    fecha_publicacion = models.DateField()