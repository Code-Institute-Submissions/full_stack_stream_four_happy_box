from django.urls import path
from .views import *




urlpatterns = [
    path('<pk>/', product_detail, name='product_detail'),
    path('', product_list, name= 'all_products'),
    
    ]