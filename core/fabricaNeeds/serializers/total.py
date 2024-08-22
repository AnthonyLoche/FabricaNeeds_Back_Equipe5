from rest_framework.serializers import ModelSerializer

from core.fabricaNeeds.models import Total

class TotalSerializer(ModelSerializer):
    class Meta:
        model = Total
        fields = ['total']