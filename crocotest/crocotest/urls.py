from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from crocod import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^croco_document/(?P<uuid>[-\w]+)$',
        views.CrocoDocumentView.as_view(redirect=True),
        name='croco_document_url'),
    url(r'^croco_document_content/(?P<uuid>[-\w]+)$',
        views.CrocoDocumentView.as_view(),
        name='croco_document_content_url'),
    url(r'^croco_document_download/(?P<uuid>[-\w]+)$',
        views.CrocoDocumentDownload.as_view(),
        name='croco_document_download'),
    url(r'^croco_thumbnail_download/(?P<uuid>[-\w]+)$',
        views.CrocoThumbnailDownload.as_view(),
        name='croco_thumbnail_download'),
    url(r'^croco_text_download/(?P<uuid>[-\w]+)$',
        views.CrocoTextDownload.as_view(),
        name='croco_text_download'),


    # Examples:
   # url(r'^$', 'crocotest.views.home', name='home'),
 #   url(r'^crocotest/', include('crocotest.crocod.urls')),

    # the djcroco url
    url(r'', include('djcroco.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
