from rest_framework import serializers
from core.fabricaNeeds.models import Pagamentos

class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = ['payment_id', 'cliente', 'email', 'cpf', 'valor', 'status', 'data_pagamento', 'data_aprovacao', 'descricao', 'pix_copiacola']