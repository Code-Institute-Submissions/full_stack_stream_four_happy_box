"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import get_index
from accounts import urls as accounts_urls
from products import urls as products_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from search import urls as search_urls
from wishlist import urls as wishlist_urls
from reviews import urls as reviews_urls
from blog import urls as blog_urls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
    path('', get_index, name='home'),
    path('products/', include(products_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('search/', include(search_urls)),
    path('wishlist/', include(wishlist_urls)),
    path('reviews/', include(reviews_urls)),
    path('blog/', include(blog_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
