from rest_framework import viewsets

from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all().order_by(
        "-created_at"
    )

    serializer_class = ComplaintSerializer