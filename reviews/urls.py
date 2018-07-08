from django.urls import path
from .views import add_a_review

urlpatterns = [
    path('add/', add_a_review, name='add_a_review'),
]