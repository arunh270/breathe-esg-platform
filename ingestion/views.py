from rest_framework.decorators import api_view
from rest_framework.response import Response

from emissions.models import EmissionRecord
from .utils import normalize_sap_record

from organizations.models import Organization
from .models import DataSource, RawRecord

import pandas as pd


@api_view(["POST"])
def upload_sap(request):

    file = request.FILES.get("file")

    if not file:
        return Response({
            "error": "No file uploaded"
        })

    # Get first organization
    organization = Organization.objects.first()

    if not organization:
        return Response({
            "error": "No organization found"
        })

    # Save uploaded file
    data_source = DataSource.objects.create(
        organization=organization,
        source_type="sap",
        uploaded_file=file
    )

    # Reset file pointer after saving
    file.seek(0)

    # Read CSV
    df = pd.read_csv(file)

    # Process rows
    for _, row in df.iterrows():

        # Save raw row
        raw_record = RawRecord.objects.create(
            data_source=data_source,
            raw_data=row.to_dict()
        )

        # Normalize row
        normalized = normalize_sap_record(
            row.to_dict()
        )

        # Save emission record
        EmissionRecord.objects.create(
            organization=organization,
            raw_record=raw_record,

            scope=normalized["scope"],
            category=normalized["category"],

            activity_value=normalized["activity_value"],
            activity_unit=normalized["activity_unit"],

            normalized_value=normalized["normalized_value"],
            normalized_unit=normalized["normalized_unit"],

            co2e_kg=normalized["co2e_kg"],

            activity_date="2026-05-25"
        )

    return Response({
        "message": "SAP file processed successfully"
    })