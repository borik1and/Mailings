from django.contrib import admin

from clients.models import Clients


@admin.register(Clients)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'name', 'surname')
    list_filter = ('name', 'surname')
