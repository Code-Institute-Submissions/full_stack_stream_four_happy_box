from django.urls import path
from .views import *


urlpatterns = [
    path('', get_products, name= 'all_products'),
    path('categories/<category>/', get_categ_products, name="categories"),
    
    ]