from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index),
    path('categories', show_categories),
    path('product', product_detail),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail')
]
