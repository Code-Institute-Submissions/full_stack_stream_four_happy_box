from django.shortcuts import get_object_or_404
from products.models import Product


def get_wishlist_items(wishlist):
    
    wishlist_items = []
    for item_id, item_quantity in wishlist.items():
        this_product = get_object_or_404(Product, pk=item_id)
        this_item = {
            'product_id': item_id, 
            "image": this_product.image,
            "name": this_product.name,
            "description": this_product.description,
            "price": this_product.price,
            'quantity': item_quantity,
        }
        wishlist_items.append(this_item)
        
    return {'wishlist_items':wishlist_items}