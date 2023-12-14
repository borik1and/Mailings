from django.urls import path
from mailing.views import MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, MailingCreateView
from .service import send

app_name = 'mailing'
sending = send('borik1and@gmail.com')

urlpatterns = [
    path('create/', MailingCreateView.as_view(), name='create'),
    path('list/', MailingListView.as_view(), name='list'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    # path('mail', send('borik1and@gmail.com'), name='mail')
]
