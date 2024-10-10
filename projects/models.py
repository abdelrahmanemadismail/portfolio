from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='technologies/icons/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects')
    image = models.ImageField(upload_to='projects/images/')
    github_link = models.URLField(max_length=200, blank=True)
    live_demo_link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    long_description = models.TextField(blank=True, null=True)  # New field for Markdown text

    def __str__(self):
        return self.title