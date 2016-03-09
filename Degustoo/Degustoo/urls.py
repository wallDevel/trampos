from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Degustoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('index.urls', namespace='index')),
    url(r'^administracao/', include('administracao.urls', namespace="administracao")),
    url(r'^restaurante/', include('restaurante.urls', namespace="restaurante")),
    url(r'^cliente/', include('cliente.urls', namespace="cliente")),
)
