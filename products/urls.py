from django.urls import path
from .views import *




urlpatterns = [
    path('<pk>/', product_detail, name='product_detail'),
    path('', product_list, name= 'all_products'),
    path('categories/<category>', get_cat_products, name="categories"),
    
    ]