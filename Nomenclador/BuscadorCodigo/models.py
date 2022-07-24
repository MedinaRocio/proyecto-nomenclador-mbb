from django.db import models

# Create your models here.

class Actividades(models.Model):
    codigo=models.IntegerField()
    nombreActividad=models.CharField(max_length=999)
    
