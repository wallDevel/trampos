from django.db import models

from django.conf import settings
# Create your models here.

# MODELS 
class Cliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
    carrinho= models.OneToOneField("Carrinho")
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.nome

class Carrinho(models.Model):
    cliente_email = models.CharField(max_length=30)