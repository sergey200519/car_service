from django.db import models
from django.conf import settings

class ArchivedOrder(models.Model):
    original_id = models.IntegerField()
    client_username = models.CharField(max_length=150)
    service_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    technician_username = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=20)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[АРХИВ] {self.service_name} для {self.client_username}"
