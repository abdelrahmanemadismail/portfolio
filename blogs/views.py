from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Category

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'tags': tags, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def tag_post_list(request, tag_slug):
    tags = Tag.objects.all()
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag, published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'tags': tags})

def category_post_list(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})