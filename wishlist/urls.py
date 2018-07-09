from django.urls import path,include
from .views import *

urlpatterns = [
    path('', view_wishlist, name="view_wishlist") ,
    path('add', add_to_wishlist, name="add_to_wishlist"),
    path('remove_wishlist_item/(<id>\d+)', remove_wishlist_item, name="remove_wishlist_item"),
    path('remove_all_wishlist_items/', delete_all_wishlist_items, name="delete_all_wishlist_items"),
    path('add_all_wishlist_items_to_cart/', add_all_wishlist_items_to_cart, name="add_all_wishlist_items_to_cart"),
]