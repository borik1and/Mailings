from django.urls import path
from users.views import UsersListView, UsersDetailView, UsersUpdateView, UsersDeleteView, UsersCreateView


app_name = 'users'


urlpatterns = [
    path('create/', UsersCreateView.as_view(), name='create'),
    path('list/', UsersListView.as_view(), name='list'),
    path('view/<int:pk>/', UsersDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', UsersUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='delete'),
]