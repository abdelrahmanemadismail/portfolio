from django.contrib import admin
from .models import Project, Technology

# Register the Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Columns to display in the admin list view
    search_fields = ('title', 'description')  # Searchable fields
    list_filter = ('created_at',)  # Filters for the admin panel
    filter_horizontal = ('technologies',)  # Makes it easier to manage ManyToMany fields

# Register the Technology model
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the technology
    search_fields = ('name',)  # Make the name searchable
