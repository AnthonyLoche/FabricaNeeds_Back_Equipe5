from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.fabricaNeeds.models import Demandas


class DemandasSerializer(ModelSerializer):
    nome_produto = serializers.SerializerMethodField()

    class Meta:
        model = Demandas
        fields = ["id", "produto", "produto_nao_cadastrado", "quantidade", "nome_produto", "data"]

    def get_nome_produto(self, obj):
        if obj.produto:
            return obj.produto.item
        return None