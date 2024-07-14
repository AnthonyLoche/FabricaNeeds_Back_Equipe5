from rest_framework import serializers
from core.fabricaNeeds.models import Pagamentos

class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = '__all__'