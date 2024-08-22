from rest_framework.viewsets import ModelViewSet

from core.fabricaNeeds.models import Demandas
from core.fabricaNeeds.serializers import DemandasSerializer

class DemandasViewSet(ModelViewSet):
    queryset = Demandas.objects.all().order_by('id')
    serializer_class = DemandasSerializer