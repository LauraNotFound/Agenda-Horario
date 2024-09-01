from django.db import models

# Create your models here: Crea tus modelos aquí
class Task(models.Model):
    actividad = models.CharField(max_length=100) # name no debe ser más largo de 100 caracteres
    dia = models.CharField(max_length=10, default='')
    hora = models.CharField(max_length=10, default='')
    color = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.actividad