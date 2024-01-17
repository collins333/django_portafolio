from django.db import models
import datetime

# Create your models here.
class Publicacion(models.Model):
  titulo = models.CharField(max_length=100)
  contenido = models.TextField()
  imagen = models.ImageField(upload_to='blog/imagenes/')
  fecha = models.DateField(datetime.date.today)
