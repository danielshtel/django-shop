from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$',
        ProductDetailView.as_view(),
        name='product_detail'),
    path('', HomeShop.as_view(), name='home'),
    path('categories', CategoryShop.as_view(), name='categories'),
]
