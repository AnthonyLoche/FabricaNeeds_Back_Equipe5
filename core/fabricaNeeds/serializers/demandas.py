from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.fabricaNeeds.models import Demandas


class DemandasSerializer(ModelSerializer):
    nome_produto = serializers.CharField(source="produto.item")
    class Meta:
        model = Demandas
        fields = ["produto", "produto_nao_cadastrado", "quantidade", "nome_produto" , "data"]
