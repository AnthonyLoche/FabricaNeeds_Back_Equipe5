from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.fabricaNeeds.models import Demandas


class DemandasSerializer(ModelSerializer):

    class Meta:
        model = Demandas
        fields = ["id", "produto", "quantidade", "data"]

    # def get_nome_produto(self, obj):
    #     if obj.produto:
    #         return obj.produto.item
    #     return None