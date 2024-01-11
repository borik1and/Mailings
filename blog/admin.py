from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'creation_date', 'publication', 'view_num')
    list_filter = ('title', 'creation_date', 'view_num')
