from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import views_default, views_cardapio, views_opcao, views_subcardapio

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'restaurante', 
#     views_rest.RestauranteRest)
# router.register(r'restaurante/(?P<r_pk>[0-9]+)/cardapio', 
#     views_rest.CardapioRest, base_name="cardapio")
# router.register(r'restaurante/cardapio/(?P<c_pk>[0-9]+)/opcao', 
#     views_rest.OpcaoRest, base_name="opcao")
# router.register(r'restaurante/cardapio/(?P<c_pk>[0-9]+)/subcardapio', 
#     views_rest.SubcardapioRest, base_name="subcardapio")
# router.register(r'restaurante/cardapio/(?P<c_pk>[0-9]+)/item', 
#     views_rest.ItemCardapioRest, base_name="itemCardapio")
# router.register(r'restaurante/subcardapio/(?P<s_pk>[0-9]+)/item', 
#     views_rest.ItemSubcardapioRest, base_name="itemCardapio")
# router.register(r'restaurante/opcao/(?P<o_pk>[0-9]+)/item', 
#     views_rest.ItemOpcaoRest, base_name="itemCardapio")

urlpatterns = [
    # DEFAULT
    url(r'^$', views_default.Index.as_view(), name="index"),
    url(r'^promoções/$', views_default.Promocoes.as_view(), name="promocoes"),
    url(r'^combos/$', views_default.Combos.as_view(), name="combos"),


    # CARDAPIO
    url(r'^criar_cardapio/$', 
        views_cardapio.CriarCardapio.as_view(), name="criar_cardapio"),
    url(r'^meus_cardapios/$', 
        views_cardapio.ListaCardapio.as_view(), name="meus_cardapios"),
    url(r'^editar_cardapio/(?P<card_id>[0-9]+)/$', 
        views_cardapio.EditarCardapio.as_view(), name="editar_cardapio"),
    url(r'^deletar_cardapio/(?P<card_id>[0-9]+)/$', 
        views_cardapio.DeletarCardapio.as_view(), name="deletar_cardapio"),
    url(r'^cardapio/(?P<card_id>[0-9]+)/$', 
        views_cardapio.CardapioView.as_view(), name="cardapio"),
    url(r'^criar_item/(?P<card_id>[0-9]+)/$', 
        views_cardapio.CriarItem.as_view(), name="criar_item"),
    url(r'^editar_item/(?P<card_id>[0-9]+)/(?P<i_id>[0-9]+)/$', 
        views_cardapio.EditarItem.as_view(), name="editar_item"),
    url(r'^deletar_item/(?P<card_id>[0-9]+)/(?P<i_id>[0-9]+)/$', 
        views_cardapio.DeletarItemCardapio.as_view(), name="deletar_item"),

    # SUBCARDAPIO
    url(r'^criar_subcardapio/(?P<card_id>[0-9]+)/$', 
        views_subcardapio.CriarSubcardapio.as_view(), name="criar_subcardapio"),
    url(r'^editar_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_subcardapio.EditarSubcardapio.as_view(), name="editar_subcardapio"),
    url(r'^deletar_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_subcardapio.DeletarSubcardapio.as_view(), name="deletar_subcardapio"),
    url(r'^subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_subcardapio.SubcardapioView.as_view(), name="subcardapio"),
    url(r'^criar_item_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_subcardapio.CriarItemSubcardapio.as_view(), name="criar_item_subcardapio"),
    url(r'^editar_item_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', 
        views_subcardapio.EditarItemSubcardapio.as_view(), name="editar_item_subcardapio"),
    url(r'^deletar_item_subcardapio/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', 
        views_subcardapio.DeletarItemSubcardapio.as_view(), name="deletar_item_subcardapio"),

    #OPCAO
    url(r'^criar_opcao/(?P<card_id>[0-9]+)/$', 
        views_opcao.CriarOpcao.as_view(), name="criar_opcao"),
    url(r'^editar_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_opcao.EditarOpcao.as_view(), name="editar_opcao"),
    url(r'^deletar_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_opcao.DeletarOpcao.as_view(), name="deletar_opcao"),
    url(r'^opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_opcao.OpcaoView.as_view(), name="opcao"),
    url(r'^criar_item_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/$', 
        views_opcao.CriarItemOpcao.as_view(), name="criar_item_opcao"),
    url(r'^editar_item_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', 
        views_opcao.EditarItemOpcao.as_view(), name="editar_item_opcao"),
    url(r'^deletar_item_opcao/(?P<card_id>[0-9]+)/(?P<id>[0-9]+)/(?P<i_id>[0-9]+)/$', 
        views_opcao.DeletarItemOpcao.as_view(), name="deletar_item_opcao"),
    url(r'^gerar_item_preco/(?P<card_id>[0-9]+)/(?P<id>[0-9])$', 
        views_opcao.ItemPriceGenerator.as_view(), name="gerar_item_preco"),
]