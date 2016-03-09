from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^registrar_avaliavel/$', RegistrarAvaliavel.as_view(), name="registrar_avaliavel"),
    url(r'^pesquisar_avaliavel/$', PesquisarAvaliavel.as_view(), name="pesquisar_avaliavel"),
]