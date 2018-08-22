from django.test import TestCase
from .models import Post, Comment


class TestPostModel(TestCase):
    def test_views_defaults_to_zero(self):
        post = Post(title='Create a Test')
        post.save()
        self.assertEqual(post.title, "Create a Test")
        self.assertEqual(post.views, 0)
        
    def test_can_create_a_post_with_a_title_and_view(self):
        post = Post(title="Create a Test", views=0)
        post.save()
        self.assertEqual(post.title, "Create a Test")
        self.assertEqual(post.views, 0)
        
    def test_post_as_a_string(self):
        post = Post(title="Create a Test")
        self.assertEqual("Create a Test", str(post))