
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from crocod import views

urlpatterns = patterns('',
    url(r'', include('djcroco.urls')),


    url(r'^$', 'crocod.views.index', name='home'),
   # url(r'^crocotest/', include('crocotest.crocod.urls')),

    url(r'', include('djcroco.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
