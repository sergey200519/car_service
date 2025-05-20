from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'technician', 'status', 'created_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    search_fields = ('client__username', 'service__name', 'technician__username')
