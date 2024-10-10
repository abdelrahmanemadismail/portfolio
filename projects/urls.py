from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),  # List view for all projects
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),  # Detail view for a specific project
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),  # Delete view for removing a project
]
