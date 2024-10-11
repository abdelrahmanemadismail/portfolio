from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Columns to display in the admin list view
    search_fields = ('title', 'description')  # Searchable fields
    list_filter = ('created_at',)  # Filters for the admin panel
    filter_horizontal = ('categories',)  # Makes it easier to manage ManyToMany fields

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the technology
    search_fields = ('name',) # Make the name searchable