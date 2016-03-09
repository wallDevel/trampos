from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'Degustoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Index.as_view(), name="index"),
    url(r'^registrar_restaurante/$', Registrar_Restaurante.as_view(), name="registrar_restaurante")
]