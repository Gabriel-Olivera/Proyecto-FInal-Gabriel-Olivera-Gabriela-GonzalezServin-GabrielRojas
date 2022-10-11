from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Electrodomesticos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50,)
    precio = models.IntegerField()
    email_contacto = models.EmailField()
    #fecha_publicacion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+" "+self.marca+" "+str(self.precio)

class Muebles(models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length=50) 
    precio = models.IntegerField()
    email_contacto = models.EmailField()
    #fecha_publicacion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+" "+self.material+" "+str(self.precio)

class Vehiculos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    email_contacto = models.EmailField()
    #fecha_publicacion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+" "+self.marca+" "+str(self.precio)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares')