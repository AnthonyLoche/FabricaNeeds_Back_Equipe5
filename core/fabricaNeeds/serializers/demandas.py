from rest_framework.serializers import ModelSerializer

from core.fabricaNeeds.models import Demandas


class DemandasSerializer(ModelSerializer):
    class Meta:
        model = Demandas
        fields = ["produto", "produto_nao_cadastrado" "quantidade", "data"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["produto"] = instance.produto.item
        return representation
