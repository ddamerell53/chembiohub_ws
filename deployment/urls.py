from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',

   (r'^', include('cbh_chembl_ws_extension.urls')),

    )

