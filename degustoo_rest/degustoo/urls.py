from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from restaurante.views import views_rest

router = routers.DefaultRouter()
router.register(r'restaurante', 
    views_rest.RestauranteRest)

router.register(r'restaurante/(?P<r_pk>[0-9]+)/cardapio', 
    views_rest.CardapioRest, base_name="cardapio")
router.register(r'restaurante/cardapio/(?P<c_pk>[0-9]+)/opcao', 
    views_rest.OpcaoRest, base_name="opcao")
router.register(r'restaurante/cardapio/(?P<c_pk>[0-9]+)/subcardapio', 
    views_rest.SubcardapioRest, base_name="subcardapio")

router.register(r'restaurante/cardapio/(?P<c_pk>[0-9]+)/item', 
    views_rest.ItemCardapioRest, base_name="itemCardapio")
router.register(r'restaurante/subcardapio/(?P<s_pk>[0-9]+)/item', 
    views_rest.ItemSubcardapioRest, base_name="itemSubcardapio")
router.register(r'restaurante/opcao/(?P<o_pk>[0-9]+)/item', 
    views_rest.ItemOpcaoRest, base_name="itemOpcao")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'degustoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('index.urls', namespace='index')),
    url(r'^administracao/', include('administracao.urls', namespace="administracao")),
    url(r'^restaurante/', include('restaurante.urls', namespace="restaurante")),
    url(r'^cliente/', include('cliente.urls', namespace="cliente")),

    url(r'^ajax/', include(router.urls)),
)
