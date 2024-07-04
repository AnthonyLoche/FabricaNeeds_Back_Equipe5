from rest_framework.viewsets import ModelViewSet

from core.fabricaNeeds.models import EntradasEstoque
from core.fabricaNeeds.serializers import EntradasEstoqueSerializer

class EntradasEstoqueViewSet(ModelViewSet):
    queryset = EntradasEstoque.objects.all()
    serializer_class = EntradasEstoqueSerializer