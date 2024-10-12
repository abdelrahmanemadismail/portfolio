from django.shortcuts import render, get_object_or_404
from blogs.models import Post, Tag, Category
from projects.models import Project, Technology

def index(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')[0:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    projects = Project.objects.all()[0:3]
    technologies = Technology.objects.all()
    return render(request, 'pages/index.html', {'posts': posts, 'tags': tags, 'categories': categories, 'projects': projects, 'technologies': technologies})