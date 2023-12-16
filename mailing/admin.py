from django.contrib import admin

from .models import Mailing


@admin.register(Mailing)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'mailing_start_time', 'mailing_stop_time', 'period', 'status',
                    'last_executed', 'attempt_status', 'server_response')
    list_filter = ('mailing_start_time', 'period', 'status', 'attempt_status')
