from django.db import models

# Create your models here.
class Proyect(models.Model):
    nombre_proyecto = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    primer_nombre = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)