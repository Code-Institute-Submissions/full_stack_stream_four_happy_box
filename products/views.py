from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def get_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products/product_list.html', {'products':products})
    
def get_categ_products(request, category):
    products = Product.objects.filter(category=category)
    print (products)
    return render(request, 'products/product_list.html', {'products':products})
    

