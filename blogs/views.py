from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_post_list(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(categories=category, published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})
