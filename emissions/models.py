from django.db import models

from organizations.models import Organization
from ingestion.models import RawRecord


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    scope = models.CharField(max_length=10)

    category = models.CharField(max_length=50)

    activity_value = models.FloatField()

    activity_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField()

    normalized_unit = models.CharField(max_length=50)

    co2e_kg = models.FloatField()

    activity_date = models.DateField()

    suspicious = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )