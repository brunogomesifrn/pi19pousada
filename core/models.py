from django.db import models

class Estilos(models.Model):
	nome = models.CharField('Nome', max_length=50)

	def __str__(self):
		return self.nome

class Dancarinos(models.Model):
	nome = models.CharField('Nome', max_length=50)
	biografia = models.CharField('Biografia', max_length=1000, null=True)
	curso = models.CharField('Curso', max_length=30)
	idade = models.IntegerField('Idade')
	foto = models.ImageField('Foto', upload_to='templates', null=True)
	estilo = models.ForeignKey(Estilos, on_delete=models.CASCADE)