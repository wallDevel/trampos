from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^registrar/$', Registrar.as_view(), name="registrar"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
]