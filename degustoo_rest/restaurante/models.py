from django.db import models

from django.conf import settings
# Create your models here.

"""
    TODO:
        Itens serao separados em grupo (pizzas salgadas, pizzas doces, etc...)
        Combo sera um cardapio, com itens mais complexos e opcoes, subcardapio, etc
        Promocoes serao aplicadas a:
            1. Cardapios - sendo que, o dono do restaurante devera colocar a pocentagem do desconto
            2. Item/ns - sendo que, o dono do restaurante colocara o(s) item(ns) e o valor sem selecionar itens
"""

class GerenciadorRestaurante(models.Model):
    email = models.EmailField()
    telefone =  models.CharField(max_length=50)
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_completo

class Restaurante(models.Model):
    KINDS = (
        (0, "Comum"),
        (1, "Diamante"),
    )

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
    gerenciador = models.OneToOneField(GerenciadorRestaurante)
    endereco = models.OneToOneField('core.Endereco')
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    imagem = models.ImageField("Logo Restaurante", upload_to="restaurant_profile", blank=True, null=True)
    tipo = models.IntegerField(choices=KINDS)

    def __str__(self):
        return self.nome

    def getEvery_menu(self):
        return self.cardapio_set.all().exclude(titulo__iexact='promoções').exclude(titulo__iexact='combos')

    def get_promocoes(self):
        return self.cardapio_set.get(titulo='Promoções')

    def get_combos(self):
        return self.cardapio_set.get(titulo='Combos')

    def hasMenu(self, title, exclusion_menu=None):
        if exclusion_menu:
            return self.cardapio_set.filter(titulo__iexact=title).exclude(pk=exclusion_menu.pk).exists()
        return self.cardapio_set.filter(titulo__iexact=title).exists()

    def save(self):
        super(Restaurante, self).save()
        if not self.hasMenu("Promoções") and not self.hasMenu("Combos"):
            Cardapio.objects.create(restaurante=self, titulo="Promoções", tipo="Especial")
            Cardapio.objects.create(restaurante=self, titulo="Combos", tipo="Especial")

class Cardapio(models.Model):
    restaurante = models.ForeignKey(Restaurante)
    imagem = models.ImageField(upload_to="menu_images/", blank=True, null=True)
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    @models.permalink
    def get_absolute_url(self):
        #from django.core.urlresolvers import reverse
        #return reverse('restaurante:cardapio', kwargs={'card_id': self.pk}) 
        return ('restaurante:cardapio', (), 
            {'card_id':self.pk}
        )

    def getEvery_item(self):
        return self.item_set.all()

    def getEvery_option(self):
        return self.opcao_set.all()

    def getEvery_submenu(self):
        return self.subcardapio_set.all()

    def itemNameIsFree(self, name):
        searchResult = self.item_set.filter(nome__iexact=name)
        if len(searchResult) != 0:
            return False
        return True

    def optionLabelIsFree(self, label):
        searchResult = self.opcao_set.filter(rotulo__iexact=label)
        if len(searchResult) != 0:
            return False
        return True

    def submenuTitleIsFree(self, title):
        searchResult = self.subcardapio_set.filter(titulo__iexact=title)
        if len(searchResult) != 0:
            return False
        return True

class Subcardapio(models.Model):
    titulo = models.CharField(max_length=50)
    cardapio = models.ForeignKey(Cardapio)

    def __str__(self):
        return self.titulo

    def getEvery_item(self):
        return self.item_set.all()

    def itemNameIsFree(self, name):
        searchResult = self.item_set.filter(nome__iexact=name)
        if len(searchResult) != 0:
            return False
        return True

class Opcao(models.Model):
    rotulo = models.CharField(max_length=50)
    cardapio = models.ForeignKey(Cardapio)

    def __str__(self):
        return self.rotulo

    def get_label(self):
        return self.rotulo

    def getEvery_item(self):
        return self.item_set.all()

    def setEvery_item_price(self, price):
        for i in self.getEvery_item():
            i.set_price(price)

    def itemNameIsFree(self, name):
        searchResult = self.item_set.filter(nome__iexact=name)
        if len(searchResult) != 0:
            return False
        return True

    def importItens(self, options):
        for option in options:
            optionItens = option.getEvery_item()
            self.makeImport(optionItens)

    def makeImport(self, itens):
        for i in itens:
            if self.itemNameIsFree(i.nome):
                item = Item(opcao=self,nome=i.nome,preco=0,ingredientes=i.ingredientes)
                item.save()

    def exportItens(self):
        return self.getEvery_item()

    
class Item(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    ingredientes = models.CharField(max_length=255, blank=True)
    cardapio = models.ForeignKey(Cardapio, blank=True, null=True)
    sub_cardapio = models.ForeignKey(Subcardapio, blank=True, null=True)
    opcao = models.ForeignKey(Opcao, blank=True, null=True)

    def __str__(self):
        return self.nome

    def get_name(self):
        return self.nome    

    def get_price(self):
        return self.preco

    def set_price(self, price):
        self.preco = price
        self.save()