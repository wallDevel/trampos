from django.db import models

from django.conf import settings
# Create your models here.
#from core.models import Endereco, Imagem

class Restaurante(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
    endereco = models.OneToOneField('core.Endereco')
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

class Cardapio(models.Model):
    restaurante = models.ForeignKey(Restaurante)
    imagem = models.OneToOneField('core.Imagem', blank=True, null=True)
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __unicode__(self):
        return self.titulo

class Subcardapio(models.Model):
    titulo = models.CharField(max_length=50)
    cardapio = models.ForeignKey(Cardapio)

    def __unicode__(self):
        return self.titulo

class Opcao(models.Model):
    rotulo = models.CharField(max_length=50)
    cardapio = models.ForeignKey(Cardapio)

    def __unicode__(self):
        return self.rotulo

    def import_itens(self, itens):
        for i in itens:
            item = self.item_set.filter(nome = i.nome)
            if not item:
                item = Item(opcao=self,nome=i.nome,preco=0,ingredientes=i.ingredientes)
                item.save()

    def export_itens(self):
        itens = self.item_set.all()
        if itens:
            return itens
        return None

    
class Item(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    ingredientes = models.CharField(max_length=255, blank=True)
    cardapio = models.ForeignKey(Cardapio, blank=True, null=True)
    sub_cardapio = models.ForeignKey(Subcardapio, blank=True, null=True)
    opcao = models.ForeignKey(Opcao, blank=True, null=True)

    def __unicode__(self):
        return self.nome
    