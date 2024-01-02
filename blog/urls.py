from django.urls import path

from blog.apps import BlogAppConfig
from blog.views import (BlogCreateView, BlogListView, BlogDetailView,
                        BlogUpdateView, BlogDeleteView)

# app_name = BlogAppConfig
app_name = 'blog'


urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),

]
