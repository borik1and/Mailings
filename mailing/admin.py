from django.contrib import admin

from django.contrib import admin

from .models import Mailing, Message


@admin.register(Mailing)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('mailing_start_time', 'mailing_stop_time', 'period', 'status', 'message')
    list_filter = ('mailing_start_time', 'period', 'status')


@admin.register(Message)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'content')
    list_filter = ('subject', 'content')
