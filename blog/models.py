from django.db import models


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)
    # imagen = models.ImageField(upload_to="/static/img/")
