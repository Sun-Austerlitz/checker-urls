from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('author', 'url', 'status_code', 'interval', 'pause', 'created', 'updated')
    list_filter = ('author', 'url', 'status_code', 'pause')
    search_fields = ('author', 'url')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('updated',)
