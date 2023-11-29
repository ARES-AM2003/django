from django.shortcuts import render
from .cart import Cart
# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    # print(cart.length())
    return render(request, 'cart/menue_cart.html')

def cart_page(request):
    return render(request,'cart/cart1.html')

