from django.shortcuts import render
from products.models import Product

# Create your views here.

def get_index(request):
    return render(request, "home/index.html")