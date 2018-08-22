from django.test import TestCase
from .forms import BlogPostForm, CommentForm

# Create your tests here.
class TestBlogForms(TestCase):
    
    def test_can_create_a_post_with_just_a_title(self):
        form = BlogPostForm({'title':'Create Tests'})
        self.assertFalse(form.is_valid())
        
    def test_can_create_a_comment_with_just_a_text_comment(self):
        form = CommentForm({'text':'Create Tests'})
        self.assertTrue(form.is_valid())
        
    def test_correct_message_for_missing_text(self):
        form = CommentForm({'text':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [u'This field is required.'])