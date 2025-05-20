from django.contrib import admin
from .models import ArchivedOrder

@admin.register(ArchivedOrder)
class ArchivedOrderAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'service_name', 'price', 'status', 'deleted_at')
    list_filter = ('status',)
    search_fields = ('client_username', 'service_name')
