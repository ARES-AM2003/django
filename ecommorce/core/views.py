from django.shortcuts import render
from product.models import Products,Catalog
from django.db.models import Q

# Create your views here.
def base(response):
    products=Products.objects.all()[0:4]
    return render(response,'core/frontpage.html',{'products':products})

def shop(response):
    products=Products.objects.all()
    catagory=Catalog.objects.all()
    active_catag=response.GET.get('catagory','')

    query=response.GET.get('query', '')
    if active_catag:
        products=products.filter(catalog__slug=active_catag)
    
    if query:
        products=products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    things_to_send={'products':products,
                    'catalog':catagory,
                    'active_catag': active_catag,
                    }
    return render(response,'core/shop.html',things_to_send)

