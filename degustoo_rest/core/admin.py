from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Endereco)
admin.site.register(Voto)
admin.site.register(Comentario)
admin.site.register(Resposta)
admin.site.register(Pedido)