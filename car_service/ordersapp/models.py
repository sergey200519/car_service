from django.db import models
from django.conf import settings
from servicesapp.models import Service

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    )
    
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, db_constraint=False)
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='assigned_orders'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service.name} для {self.client.username}"
