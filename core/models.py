from django.db import models
from django.contrib.auth.models import User

class Apartamento(models.Model):
	nome = models.CharField('Nome', max_length=50)
 	

	def __str__(self):
		return self.nome

class Reservar(models.Model):
	adultos = models.IntegerField('Quantos Adultos')
	apartamentos = models.ManyToManyField(Apartamento)
	quantidade = models.IntegerField('Informe a quantidade de Apartamentos Solicitados')
	criancas = models.IntegerField('Quantas Crianças')
	cpf = models.IntegerField('Informar o CPF')
	cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	cafe = models.BooleanField('Apartamento com Café da Manhã?', null=True)
	celular = models.IntegerField('Informe o Número do seu celular')
	entrada = models.DateField('Informe a sua Data de Entrada')
	saida = models.DateField('Informe a sua Data de Saída')


	def __str__(self):
		return self.cliente.username

		'''
Informar data de entrada 
Informar data de saída
Tipo de apartamento
	. individual
	. duplo
	. triplo
	. Quadruplo
Informar quantos Adultos 

Informar quantas Crianças
[
Ter informações referentes que a apartir de tal idade da criança, vai começar a cobrar.
]

Apartamento com Café da manhã?
Sim ou Não

E-mail do cliente


CPF: 

Celular:


Campo informando como funciona o procedimento de reserva.


Botão Enviar










		'''