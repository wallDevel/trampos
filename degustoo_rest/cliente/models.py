from django.db import models

from django.conf import settings
# Create your models here.

"""
    TODO:
        A entidade carrinho nao existe mais, visto que os itens serao adicionados ao cookie ou session.
        No lado client e em formato json.
            {
                "pedido": {
                    "itens": [
                        {
                            "item": {
                                "item_modifier": {
                                    "pk": id_number,
                                },
                                "opcao": {
                                    "pk": id_number,
                                },
                                "subcardapios: [
                                    {
                                        "subcardapio": {
                                            "pk": id_number,
                                            "value": add_price,
                                        },
                                    }
                                ],
                                "itens": [
                                    {
                                        "item": {
                                            "pk": id_number,
                                            "value": price,
                                        },
                                    },
                                ],
                            },
                        },
                    ],
                }
            }
"""


# MODELS 
class Cliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    imagem = models.ImageField("Foto Perfil", upload_to="user_profile/", blank=True, null=True)
    
    def __str__(self):
        return self.nome