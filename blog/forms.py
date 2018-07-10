from django import forms
from .models import Post, Comment, User

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)