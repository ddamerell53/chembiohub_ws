"""Main url conf for the ChemBio Hub Platform app which is imported by the deployment urls.py"""
from django.conf.urls import patterns, url, include
from cbh_core_api.resources import Login, Logout
from django.conf import settings
from cbh_core_api import flowjs_urls as cbh_flow
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done, password_reset, password_reset_done, password_reset_complete, password_reset_confirm


from tastypie.api import Api
from cbh_chem_api.resources import *
from cbh_chem_api.compounds import *

from cbh_core_api.resources import *
from cbh_core_api.views import *
from django.conf import settings
DEFAULT_API_NAME = 'chemblws'

try:
    api_name = settings.WEBSERVICES_NAME
    print api_name
except AttributeError:
    api_name = DEFAULT_API_NAME

from cbh_core_api.resources import ProjectTypeResource

api = Api(api_name=api_name)
api.register(ProjectTypeResource())
api.register(CBHCompoundUploadResource())
api.register(CBHCompoundBatchResource())
api.register(UserResource())
api.register(ChemRegDataPointProjectFieldResource())
api.register(ChemRegCustomFieldConfigResource())
api.register(ChemregProjectResource())
api.register(SkinningResource())
api.register(InvitationResource())
api.register(ProjectPermissionResource())
api.register(CBHFlowFileResource())
api.register(CBHFlowFileDownloadResource())
admin.autodiscover()
api.register(CBHSavedSearchResource())
api.register(CBHChemicalSearchResource())
api.register(CBHPlateMapResource())


from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^%s/login' % api_name.split("/")
                           [0], Login.as_view(), name="login"),
                       url(r'^%s/logout' %
                           api_name, Logout.as_view(), name="logout"),
                       #change password outside of admin
                       url(r'^%s/password_change' %
                           api_name, password_change, {'template_name': 'cbh_chem_api/password_change.html'}, name="password_change"),
                       url(r'^%s/password_change_done' %
                           api_name, password_change_done, {'template_name': 'cbh_chem_api/password_change_done.html'}, name="password_change_done"),
                       url(r'^%s/password_reset' %
                           api_name, password_reset, {'from_email': 'no-reply-chemireg@chembiohub.ox.ac.uk', 'template_name':'cbh_chem_api/password_reset.html'}, name="password_reset"),
                       url(r'^%s/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})' %
                           api_name, password_reset_confirm, {'template_name': 'cbh_chem_api/password_reset_confirm.html'}, name="password_reset_confirm"),
                       url(r'^%s/password_reset/done' %
                           api_name, password_reset_done, {'template_name': 'cbh_chem_api/password_reset_done.html'}, name="password_reset_done"),
                       url(r'^%s/reset/done' %
                           api_name, password_reset_complete, {'template_name': 'cbh_chem_api/password_reset_complete.html'}, name="password_reset_complete"),
                       # adding this to allow configured upload URL within
                       # django-flowjs
                       #we can deprecate the urls from flow when the time is right
                       url(r'^%s/flowv2/' % api_name, include(cbh_flow)),
                       url(r'^%s/admin/' % api_name, include(admin.site.urls)),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^%s/$' % api_name.split("/")
                           [0], login_required(Index.as_view()))

                       )

urlpatterns += api.urls

if "django_webauth" in settings.INSTALLED_APPS:
    from django_webauth.views import LoginView, LogoutView

    urlpatterns += patterns('',
                            url(r'^%s/webauth' % api_name.split("/")
                                [0], LoginView.as_view(), name="webauthlogin"),
                            url(r'^%s/webauthlogout' % api_name.split("/")
                                [0], LogoutView.as_view(), name="webauthlogout"),
                            )
