from django.db import models


from organizations.models import Organization

class DataSource(models.Model):

    SOURCE_TYPES = [
        ("sap", "SAP"),
        ("utility", "Utility"),
        ("travel", "Travel"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(max_length=20)

    uploaded_file = models.FileField(
        upload_to="uploads/"
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)


class RawRecord(models.Model):

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    raw_data = models.JSONField()

    processing_status = models.CharField(
        max_length=20,
        default="pending"
    )

    error_message = models.TextField(
        blank=True
    )

