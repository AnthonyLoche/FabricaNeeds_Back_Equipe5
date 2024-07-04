from rest_framework.viewsets import ModelViewSet

from core.fabricaNeeds.models import Total
from core.fabricaNeeds.serializers import TotalSerializer

class TotalViewSet(ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer