from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', HomeShop.as_view(), name='home'),
    path('categories', CategoryShop.as_view(), name='categories'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        ProductDetailView.as_view(),
        name='product_detail')
]
