from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import BlogPostForm, CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/blog_posts.html", {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/post_detail.html", {'post': post})
    
def new_post(request):
    if request.method == "POST":
        #request.FILES if you are entering images
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = BlogPostForm()
        
    return render(request, 'posts/blog_post_form.html', {'form': form})
        
        
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if not(request.user == post.author or request.user.is_superuser):
        return HttpResponseForbidden()
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.pk)        
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'posts/blog_post_form.html', {'form': form})

@login_required    
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Thanks for your feedback. Your comment will appear once approved")
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment_to_post.html', {'form': form})
    

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if not request.user.is_superuser :
        return HttpResponseForbidden('You do not have permission to approve!')
    else:
        comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to approve!')
    else:
        comment.delete()
    return redirect('post_detail', pk=comment.post.pk)