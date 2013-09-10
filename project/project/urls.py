from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('lemonpi.urls')),
    #Here I am wiring the root url to include the lemonpi URLS which will be coded later.
)
