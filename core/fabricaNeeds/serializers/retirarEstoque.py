from rest_framework.serializers import ModelSerializer

from core.fabricaNeeds.models import RetirarEstoque

class RetirarEstoqueSerializer(ModelSerializer):
    class Meta:
        model = RetirarEstoque
        fields = "__all__"