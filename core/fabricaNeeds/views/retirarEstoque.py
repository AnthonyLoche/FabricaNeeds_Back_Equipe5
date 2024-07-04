from rest_framework.viewsets import ModelViewSet

from core.fabricaNeeds.models import RetirarEstoque
from core.fabricaNeeds.serializers import RetirarEstoqueSerializer

class RetirarEstoqueViewSet(ModelViewSet):
    queryset = RetirarEstoque.objects.all()
    serializer_class = RetirarEstoqueSerializer