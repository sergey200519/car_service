from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_deleted')
    list_filter = ('is_deleted',)
    search_fields = ('name',)
