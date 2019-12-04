from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(null=True)
    clasificacion = models.CharField(max_length=30)
    precio= models.IntegerField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    producto = models.ForeignKey(
    Producto, null=True, blank=True, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True, null=True)
    comuna = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
    