from django.contrib import admin

from restaurante.models import *

# Register your models here.
admin.site.register(GerenciadorRestaurante)
admin.site.register(Restaurante)
admin.site.register(Subcardapio)
admin.site.register(Cardapio)
admin.site.register(Opcao)
admin.site.register(Item)