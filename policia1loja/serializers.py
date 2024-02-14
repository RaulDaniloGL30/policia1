from rest_framework import serializers
from .models import OrdenCombustible
from django.utils import timezone

class OrdenCombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenCombustible
        fields = '__all__'  # o una lista de los campos que se desea incluir


    def create(self, validated_data):
        validated_data['Fecha'] = validated_data.get('Fecha', timezone.now().date())
        return super().create(validated_data)