from __future__ import unicode_literals
from django.db import models

# Create your models here.

ESTADO = (
	('1', 'Activo'),
	('2', 'Inactivo')
)

class Terapia(models.Model):
	id_terapia = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=50)
	limite = models.IntegerField()
	estado = models.CharField(max_length=20, choices=ESTADO)
