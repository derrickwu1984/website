from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
from interface.views import get_params,get_headers,search,func_add
import xadmin
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^trs_code/(?P<trs_code>\w*)/$',get_params),
    url(r'^header/$',get_headers),
    url(r'^search/$', search, name='search'),
    url(r'^func_add/$', func_add, name='func_add'),
    url(r'^save_record/$', func_add, name='func_add'),

]
