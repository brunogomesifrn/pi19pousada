from django.db import models
from django.contrib.auth.models import User


class Reservar(models.Model):
	nome = models.CharField('Nome', max_length=50)

	def __str__(self):
		return self.nome

class usuarios(models.Model):
	nome = models.CharField('Nome', max_length=50)
	biografia = models.CharField('Biografia', max_length=1000, null=True)
	cpf = models.CharField('cpf', max_length=14)
	idade = models.IntegerField('Idade')
	foto = models.ImageField('Foto', upload_to='templates', null=True)
	