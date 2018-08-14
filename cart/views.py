from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from decimal import Decimal
from django.contrib import messages
from .utils import get_cart_items_and_total

# Create your views here.

def view_cart(request):
    cart=request.session.get('cart', {})
    print(cart)
    if len(cart) == 0:
       return render(request, "cart/empty_cart.html")
    context = get_cart_items_and_total(cart)
    return render(request, "cart/view_cart.html", context)
    

def add_to_cart(request):
    id = request.POST['id']
    if int(request.POST['quantity']) > 0:
        quantity = int(request.POST['quantity'])
    else:
        quantity = 1
        
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
   
    print(cart)
    request.session['cart'] = cart   
    messages.success(request, "You added to your cart")
    return redirect(request.GET.get('next', 'products'))
    
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')  


def adjust_cart(request, id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST['quantity'])
    if quantity > 0:
        cart[id] = quantity
    else:
        del cart[id]
        
    request.session['cart'] = cart
    return redirect('view_cart')