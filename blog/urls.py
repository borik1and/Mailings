from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import (BlogCreateView, BlogListView, BlogDetailView,
                        BlogUpdateView, BlogDeleteView)

app_name = 'blog'

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list', cache_page(60)(BlogListView.as_view()), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),

]
