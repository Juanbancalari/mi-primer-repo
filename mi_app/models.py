from unittest.util import _MAX_LENGTH
from django.db import models

class Curso(models.Model):

    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()
    

    def __str__(self):
        return f"{self.nombre} {self.camada}"

class Familia(models.Model):

    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()


