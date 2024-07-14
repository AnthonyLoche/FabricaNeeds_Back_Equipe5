from rest_framework.viewsets import ModelViewSet

from core.fabricaNeeds.models import Pagamentos
from core.fabricaNeeds.serializers import PagamentosSerializer

class PagamentosViewSet(ModelViewSet):
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializer