from django.contrib import admin
from django.urls import path
from . import views
from product.views import proDetail



urlpatterns = [
    path('',views.base,name='base'),
    path('shop/',views.shop,name='shop'),
    path('shop/<slug:slug>',proDetail,name='proDetail'),

]

