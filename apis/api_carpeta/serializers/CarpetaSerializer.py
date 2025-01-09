from rest_framework import serializers
from ..models.ModeloCarpeta import ModeloCarpeta

class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloCarpeta
        fields = [
            'codigo_interno',
            'nro_dim',
            'canal',
            'modalidad_despacho',
            'importador',
            'aduana_despacho',
            'clasificacion_carpeta',
            'fecha_apertura',
            'mercaderia'
        ]
