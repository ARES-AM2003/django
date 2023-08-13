from django.shortcuts import render
from .models import Products

# Create your views here.
def product(response,slug):
    product=Products.objects.get(slug=slug)
    return render(response,'product/prodDetail.html', {'product':product} )
