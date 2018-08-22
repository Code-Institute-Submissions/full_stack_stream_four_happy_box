from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post

class TestBlogViews(TestCase):
    
    def test_get_blog_posts(self):
        page=self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "posts/blog_posts.html", "base.html")
        
    def test_get_add_new_post_page(self):
        page=self.client.get("/blog/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "posts/blog_post_form.html", "base.html")
    
    # def test_get_edit_post_page(self):
    #     post = Post(title='Create a Test', content='Lorem Ipsum', tag='happy')
    #     post.save()
    #     page=self.client.get("/blog/{0}/edit/".format(post.id))
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "posts/blog_post_form.html", "base.html")
    
    def test_get_edit_post_page_for_post_that_does_not_exist(self):
        page=self.client.get("/blog/1/edit")
        self.assertEqual(page.status_code, 404)
        
    def test_get_post_detail_page(self):
        post = Post(title="Create a Test")
        post.save()
        page = self.client.get("/blog/{0}/".format(post.pk))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "posts/post_detail.html", "base.html")
    
    # def test_post_add_new(self):
    #     User.objects.create_user(
    #         username='user1', 
    #         email='user1@example.com',
    #         password='password1')
    #     self.client.login(username='user1', password='password1')
    #     response = self.client.post("/blog/new/", {"title": "Create a Test"})
    #     post = get_object_or_404(Post, pk=1)
        
    
    # def test_post_edit_a_post(self):
    #     post = Post(title = "Create a Test")
    #     post.save()
    #     id = post.id
        
    #     response = self.client.post("/blog/{0}/edit/".format(id), {"title": "A different post"})
    #     post = get_object_or_404(Post, pk=id)
        
    #     self.assertEqual("A different post", post.title)