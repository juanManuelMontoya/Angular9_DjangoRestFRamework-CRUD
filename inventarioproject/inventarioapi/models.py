from django.db import models

class Producto (models.Model):
    id_producto = models.IntegerField
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)


# Create your models here.
