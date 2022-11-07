import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    market_values = ArrayField(models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True), size=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
