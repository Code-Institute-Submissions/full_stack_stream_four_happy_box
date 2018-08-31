from django.apps import apps
from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Product

class TestBlogViews(TestCase):
    
    def test_get_product_list(self):
        page=self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/product_list.html", "base.html")
        
    def test_add_product(self):
        product = Product(name='Test Name',
                          description='Test Description')
        self.assertEqual(product.name, 'Test Name')
        self.assertEqual(product.description, "Test Description")
        self.assertFalse(product.image)
        self.assertFalse(product.price)
    
   
   