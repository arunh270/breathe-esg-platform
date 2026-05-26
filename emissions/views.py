from django.shortcuts import render


from rest_framework.generics import ListAPIView

from .models import EmissionRecord
from .serializers import (
    EmissionRecordSerializer
)

class EmissionListView(ListAPIView):

    queryset = EmissionRecord.objects.all()

    serializer_class = (
        EmissionRecordSerializer
    )
