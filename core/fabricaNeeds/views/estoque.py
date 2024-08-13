from rest_framework.viewsets import ModelViewSet

from core.fabricaNeeds.models import Estoque
from core.fabricaNeeds.serializers import EstoqueSerializer

class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

    def list(self, request, *args, **kwargs):
        
        return super().list(request, *args, **kwargs)