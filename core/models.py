from django.db import models


class Reservar(models.Model):
	nome = models.CharField('Nome', max_length=50)

	def __str__(self):
		return self.nome
