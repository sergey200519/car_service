from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.price} руб)"
