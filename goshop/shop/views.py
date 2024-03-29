from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
# changed by me
from .models import Product, Contact
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = { item['category'] for item in catprods }
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'no_of _slides':nSlides, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products, range(1,  nSlides), nSlides],
    #             [products, range(1,  nSlides), nSlides]]
    params = {'allProds' :allProds}
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    
    if request.method=="POST":
        
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        print(name, email, phone, desc)
        contact= Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")
def productView(request, myid):
    product = Product.objects.filter(id= myid)
    print(product)

    return render(request, "shop/productView.html", {'product': product[0]})

def track(request):
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def checkout(request):
    return render(request, "shop/checkout.html")

# done db to html
def pro_db(request):
    product_list = Product.objects.all()
    return render(request, "shop/pro_db.html", {'backpanel': product_list})



