
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from crocod import views

urlpatterns = patterns('',
    url(r'', include('djcroco.urls')),

    # Simple index                
    url(r'^$', 'crocod.views.index', name='index'),
    # url(r'^crocotest/', include('crocotest.crocod.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
