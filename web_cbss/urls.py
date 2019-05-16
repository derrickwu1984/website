from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
from interface.views import get_params,get_headers,search,interface_add,save_record,field_modify,field_add,field_del,field_del_save
import xadmin
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^trs_code/(?P<trs_code>\w*)/$',get_params),
    url(r'^header/$',get_headers),
    url(r'^search/$', search, name='search'),
    url(r'^func_add/$', interface_add, name='func_add'),
    url(r'^save_record/$', save_record, name='save_record'),
    url(r'^field_modify/(?P<trs_code>\w*)/$', field_modify, name='field_modify'),
    url(r'^field_add/(?P<trs_code>\w*)$', field_add, name='field_add'),
    url(r'^field_del/(?P<trs_code>\w*)$', field_del, name='field_del'),
    url(r'^field_del_save/$', field_del_save, name='field_del_save'),





]
