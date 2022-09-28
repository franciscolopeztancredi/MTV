from django.db import models

# Create your models here.
class Familia(models.Model):
  
  nombre = models.CharField(max_length=80)
  apellido = models.CharField(max_length=60)
  parentesco = models.CharField(max_length=60)
  altura = models.IntegerField()
  cumpleanios = models.DateField()