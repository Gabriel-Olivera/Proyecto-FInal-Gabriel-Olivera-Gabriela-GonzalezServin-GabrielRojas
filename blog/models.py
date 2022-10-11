from django.db import models
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.titulo + "|" + self.subtitulo