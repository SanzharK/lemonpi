from django.conf.urls import patterns, url
from rest_framework import viewsets, routers

urlpatterns = patterns('lemonpi.views',
    url(r'^users/$','user_list'),
    url(r'^users$','user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', 'user_detail'),
)
