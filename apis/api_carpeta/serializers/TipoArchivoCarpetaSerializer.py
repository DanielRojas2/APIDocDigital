from rest_framework import serializers
from ..models.ModeloTipoArchivoCarpeta import ModeloTipoArchivoCarpeta

class TipoArchivoCarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloTipoArchivoCarpeta
        fields = ['id', 'carpeta', 'tipo_archivo']
