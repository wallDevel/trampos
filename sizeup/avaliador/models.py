from django.db import models
from django.conf import settings
# Create your models here.

class Avaliador(models.Model):
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
	nome_completo = models.CharField(max_length=50)
	cpf = models.CharField(max_length=50)
	data_nascimento = models.DateField()

	def __unicode__(self):
		return self.nome_completo