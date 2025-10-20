from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"