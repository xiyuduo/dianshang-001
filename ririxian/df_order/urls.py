
from django.conf.urls import url,include
from django.contrib import admin
from  df_order import  views
urlpatterns = [
    url(r'^$', views.order),
    url(r'^addorder/$', views.order_handle),
    url(r'^pay&(\d+)/$', views.pay),
]
