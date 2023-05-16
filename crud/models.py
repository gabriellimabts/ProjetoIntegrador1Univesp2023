from django.db import models

class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	idade = models.CharField(max_length=100)
	sexo = models.CharField(max_length=1)
	salario = models.IntegerField()

	def __str__(self):
		return self.nome
