from rest_framework import serializers
from .models import TipoEmpresas


class TipoEmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoEmpresas
        fields =['id_tipo_empresa','estado_tipo_empresa','nombre_tipo_empresa']
        read_only_fields = ('id_tipo_empresa',)