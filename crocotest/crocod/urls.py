# djcroco app urls.py
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('djcroco.urls')),
)                    
