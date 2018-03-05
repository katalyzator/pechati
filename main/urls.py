from django.conf.urls import url

from main.views import *

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^contacts/$', contacts_view, name='contacts_view'),
    url(r'^products/$', goods_view, name='products'),
]
