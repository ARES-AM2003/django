from django.contrib import admin
from .models import Catalog,Products

# # Register your models here.
# class ProductAdmin(admin.ModelAdmin): # new
#      readonly_fields = ['imgpreview']
admin.site.register(Catalog)
admin.site.register(Products)
