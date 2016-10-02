from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Terapia(models.Model):
	id_terapia = models.IntegerField(primary_key=True)
	id_paciente = models.IntegerField()
	id_cita = models.IntegerField()
	recibida = models.CharField(max_length=2)
