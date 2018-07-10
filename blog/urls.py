from django.urls import path
from .views import *

urlpatterns = [
    path('new/', new_post, name='new_post'),
    path('<int:pk>/edit', edit_post, name='edit_post'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('', get_posts, name= 'get_posts'),
    path('post/(<pk>\d+)/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/(<pk>\d+)/approve/', comment_approve, name='comment_approve'),
    path('comment/(<pk>\d+)/remove/', comment_remove, name='comment_remove'),
    ]