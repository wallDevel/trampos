from django.db import models
from django.conf import settings
# Create your models here.
class Avaliavel(models.Model):
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
	nome = models.CharField(max_length=50)
	cnpj = models.CharField(max_length=50)
	razao_social = models.CharField(max_length=100)
	nome_fantasia = models.CharField(max_length=100)
	email_institucional = models.EmailField()

	def __unicode__(self):
		return self.nome_fantasia

class Avaliavel_Beta(models.Model):
	nome = models.CharField(max_length=100)
	telefone = models.CharField(max_length=50, blank=True)
	setor = models.CharField(max_length=100)
	subsetor = models.CharField(max_length=100, blank=True)
	endereco_beta = models.OneToOneField('core.Endereco_Beta', blank=True, null=True)

	def __unicode__(self):
		return self.nome

class Responsavel(models.Model):
	nome = models.CharField(max_length=50)
	email = models.EmailField()
	cnpj = models.CharField(max_length=50) 
	telefone = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nome