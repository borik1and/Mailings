from django.contrib import admin

from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'name', 'surname')
    list_filter = ('name', 'surname')

