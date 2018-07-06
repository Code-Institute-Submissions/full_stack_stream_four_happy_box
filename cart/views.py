from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.

def view_cart(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, id):
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect('all_products')
    
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect('view_cart')
    
    