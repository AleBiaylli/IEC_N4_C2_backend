from django.db import models

class programmer(models.Model):
    Nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Nombre


class Sistema(models.Model):
    nombre_sistema = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_sistema} {self.version}"