from rest_framework import serializers
from .models import Empresas

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ['id_empresa','direccion_empresa','nombre_empresa','telefono_empresa','id_tipo_empresa']
        read_only_fields = ('id_empresa',)