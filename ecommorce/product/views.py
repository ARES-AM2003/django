from django.shortcuts import render
from .models import Products

# Create your views here.
def product(request,slug):
    product=Products.objects.get(slug=slug)
    return render(request,'product/prodDetail.html', {'product':product} )
