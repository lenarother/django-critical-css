from django.contrib import admin

from .models import Critical


@admin.register(Critical)
class CriticalAdmin(admin.ModelAdmin):
    list_display = ('url', 'path', 'date_updated', 'is_pending')
    list_filter = ('is_pending',)
    search_fields = ('url',)
