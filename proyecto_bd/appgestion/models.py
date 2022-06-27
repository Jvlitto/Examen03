from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido_paterno=models.CharField(max_length=30)
    apellido_materno=models.CharField(max_length=30)
    edad=models.IntegerField()
    vacuna=models.CharField(max_length=30)
    fecha=models.CharField(max_length=30)
