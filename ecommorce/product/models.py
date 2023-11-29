from django.db import models
from django.utils.html import mark_safe
from PIL import Image
from django.core.files import File
from io import BytesIO

# Create your models here.
class Catalog(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField()
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Products(models.Model):
    catalog=models.ForeignKey(Catalog,related_name='product',on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to = 'media/',blank=True,null=True)
    name=models.CharField(max_length=200)
    slug=models.SlugField()
    description=models.TextField(blank=True,null=True)
    price=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_time',)
    
    def __str__(self):
        return self.name