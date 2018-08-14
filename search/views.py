from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if len(products) == 0:
       return render(request, "search/empty_search.html")
    return render(request, "products/product_list.html", {'products':products})