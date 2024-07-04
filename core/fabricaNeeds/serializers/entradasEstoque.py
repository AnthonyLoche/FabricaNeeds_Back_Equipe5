from rest_framework.serializers import ModelSerializer

from core.fabricaNeeds.models import EntradasEstoque

class EntradasEstoqueSerializer(ModelSerializer):
    class Meta:
        model = EntradasEstoque
        fields = "__all__"