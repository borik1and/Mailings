from django.urls import path
from mailing.views import (MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView,
                           MailingCreateView, send_mail)


app_name = 'mailing'


urlpatterns = [
    path('create/', MailingCreateView.as_view(), name='create'),
    path('list/', MailingListView.as_view(), name='list'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    path('send/', send_mail, name='send_mail'),

]
