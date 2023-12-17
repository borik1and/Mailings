from django.urls import path
from mailing.views import (MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView,
                           MailingCreateView, mailing_log)


app_name = 'mailing'


urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('logs/', mailing_log, name='logs'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),


]
