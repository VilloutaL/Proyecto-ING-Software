# Create your models here.
from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    

    def __str__(self):
        return self.usuario  
