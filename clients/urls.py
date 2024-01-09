from django.urls import path
from django.views.decorators.cache import cache_page

from clients.views import ClientsListView, ClientsDetailView, ClientsUpdateView, ClientsDeleteView, ClientsCreateView, \
    View_blogDetailView, BlogView

app_name = 'clients'


urlpatterns = [
    path('main/', BlogView.as_view(), name='main'),
    path('view_blog/<int:pk>/', View_blogDetailView.as_view(), name='view_blog'),
    path('create/', ClientsCreateView.as_view(), name='create'),
    path('list/', cache_page(60)(ClientsListView.as_view()), name='list'),
    path('view/<int:pk>/', ClientsDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ClientsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ClientsDeleteView.as_view(), name='delete'),
]