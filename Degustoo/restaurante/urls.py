from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import *

urlpatterns = [
    # DEFAULT
    url(r'^$', Index.as_view(), name="index"),

    # CARDAPIO
    url(r'^criar_cardapio/$', CriarCardapio.as_view(), name="criar_cardapio"),
    url(r'^meus_cardapios/$', ListaCardapio.as_view(), name="meus_cardapios"),
    url(r'^editar_cardapio/(?P<card_id>[0-9]+)/$', EditarCardapio.as_view(), name="editar_cardapio"),
    url(r'^deletar_cardapio/(?P<card_id>[0-9]+)/$', DeletarCardapio.as_view(), name="deletar_cardapio"),
    url(r'^cardapio/(?P<card_id>[0-9]+)/$', Cardapio_.as_view(), name="cardapio"),
    url(r'^criar_item/(?P<card_id>[0-9]+)/$', CriarItem.as_view(), name="criar_item"),
    url(r'^editar_item/(?P<card_id>[0-9]+)/(?P<i_id>[0-9]+)/$', EditarItem.as_view(), name="editar_item"),
    url(r'^deletar_item/(?P<card_id>[0-9]+)/(?P<i_id>[0-9]+)/$', DeletarItemCardapio.as_view(), name="deletar_item"),

    # SUBCARDAPIO
    url(r'^criar_subcardapio/(?P<card_id>[0-9]+)/$', CriarSubcardapio.as_view(), name="criar_subcardapio"),
    url(r'^editar_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', EditarSubcardapio.as_view(), name="editar_subcardapio"),
    url(r'^deletar_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', DeletarSubcardapio.as_view(), name="deletar_subcardapio"),
    url(r'^subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', Subcardapio_.as_view(), name="subcardapio"),
    url(r'^criar_item_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', CriarItemSubcardapio.as_view(), name="criar_item_subcardapio"),
    url(r'^editar_item_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', EditarItemSubcardapio.as_view(), name="editar_item_subcardapio"),
    url(r'^deletar_item_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', DeletarItemSubcardapio.as_view(), name="deletar_item_subcardapio"),

    #OPCAO
    url(r'^criar_opcao/(?P<card_id>[0-9]+)/$', CriarOpcao.as_view(), name="criar_opcao"),
    url(r'^editar_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', EditarOpcao.as_view(), name="editar_opcao"),
    url(r'^deletar_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', DeletarOpcao.as_view(), name="deletar_opcao"),
    url(r'^opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', Opcao_.as_view(), name="opcao"),
    url(r'^criar_item_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', CriarItemOpcao.as_view(), name="criar_item_opcao"),
    url(r'^editar_item_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', EditarItemOpcao.as_view(), name="editar_item_opcao"),
    url(r'^deletar_item_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', DeletarItemOpcao.as_view(), name="deletar_item_opcao"),
]