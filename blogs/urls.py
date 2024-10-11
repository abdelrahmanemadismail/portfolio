from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:tag_slug>/', views.tag_post_list, name='tag_post_list'),
    path('category/<str:category_slug>/', views.category_post_list, name='category_post_list'),
]
