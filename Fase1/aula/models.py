from django.db import models

class usuario (models.Model):
    email = models.EmailField()
    contraseña = models.CharField(max_length=20)
    def __str__(self) :
        return self.email
    
# Create your models here.
