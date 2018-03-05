from django.conf.urls import url

from main.views import *

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^contacts/$', contacts_view, name='contacts_view'),
    url(r'^products/$', goods_view, name='products'),
    url(r'^products/(?P<id>\d+)/$', product_detail, name='single_product'),
    url(r'^application/', application_view, name='application'),
]
