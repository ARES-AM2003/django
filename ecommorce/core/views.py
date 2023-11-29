from django.shortcuts import render,redirect,HttpResponse
from product.models import Products,Catalog
from django.db.models import Q
from .forms import Signupform
from django.contrib.auth import login, authenticate,get_user_model
from django.contrib.auth.models import User 

# Create your views here.
def base(request):
    products=Products.objects.all()

    return render(request,'core/frontpage.html',{'products':products})
def signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        # //dlkfldkflkdlfk
    
        print(form.is_valid)

        # //////////////////
        if not form.is_valid:
            form=Signupform()
            return render(request,'core/signup.html',{'form':form})
        else:
            user=form.save()

            login(request, user)
            return redirect('/')
        # else:
        #     form=Signupform()
        #     return render(request,'core/signup.html')
    else:
        form=Signupform()
    return render(request,'core/signup.html', {'form':form})
# def log_in(request):   django have built in function for login it uses views.LoginView.as_view(template_name='url of login template ie core/login.html') function for url
#     if request.method=='POST':
#         username1=request.POST.get('username')
#         # username=User.objects.get()
#         pass1=request.POST.get('password')
#         print(username1,pass1)
#         user1=authenticate(request,username=username1,password=pass1)
#         print(user1)
#         if user1 is not None:
#             login(user1)
            
#         else:
#             return redirect('/shop')

#     return render(request,'core/login.html')

def shop(request):
    products=Products.objects.all()
    catagory=Catalog.objects.all()
    active_catag=request.GET.get('catagory','')

    query=request.GET.get('query', '')
    if active_catag:
        products=products.filter(catalog__slug=active_catag)
    
    if query:
        products=products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    things_to_send={'products':products,
                    'catalog':catagory,
                    'active_catag': active_catag,
                    }
    return render(request,'core/shop.html',things_to_send)

def check_username(request):
    usern=request.POST.get('username')
    if get_user_model().objects.filter(username=usern).exists():
        return HttpResponse('Username already taken')
    else:
        return HttpResponse('uname avalilabel')