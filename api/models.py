from django.db import models

# Create your models here.
class programmer(models.Model):

    Nombre = models.CharField(max_length=100) 
Usuario = models.CharField(max_length=100) 
Idioma = models.CharField(max_length=100) 
Edad = models.PositiveSmallIntegerField() 
is_active = models.BooleanField(default=True)