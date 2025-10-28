from rest_framework import serializers
from .models import TipoContratos

class TipoContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContratos
        fields = ['id_contrato', 'nombre_contrato']
        read_only_fields = ('id_contrato',)

