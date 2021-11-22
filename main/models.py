from django.db import models

# Create your models here.


class Producto(models.Model):
    descripcion = models.CharField(max_length=160)
    precio = models.FloatField()
    nombre = models.CharField(max_length=30, default='')


class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.PositiveIntegerField()
    email = models.CharField(max_length=60)
    direccion = models.CharField(max_length=150, null=True)


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lista_productos = models.ManyToManyField(Producto)
    fecha_y_hora = models.DateTimeField()
