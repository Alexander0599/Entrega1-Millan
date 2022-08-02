#from enum import unique
from django.db import models

# Create your models here.
class mifamilia(models.Model):

    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    celular = models.IntegerField()
    correo = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} - {self.cargo}"

class ferreteria(models.Model):

    nombre_elemen = models.CharField(max_length=30)
    referencia = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio_uni = models.IntegerField()
    precio_cos = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre_elemen} - {self.referencia} - {self.cantidad}"

    class Meta():
        ordering = ("nombre_elemen", "referencia", "-cantidad")
        #unique_together = ("referencia",)


class ventas(models.Model):

    nombre_element =  models.CharField(max_length=30)
    referencia_pro = models.CharField(max_length=30)
    cantidad_ven = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre_element} - {self.referencia_pro} - {self.cantidad_ven}"

    class Meta():
        ordering = ("nombre_element", "referencia_pro", "cantidad_ven", "precio")
