from rest_framework import serializers
from ..models.ModeloDocumentoSoporte import ModeloDocumentoSoporte

class DocumentoSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDocumentoSoporte
        fields = [
            'id',
            'carpeta_tipoarchivo',
            'codigo_referencia',
            'respaldo',
            'estado_archivo',
            'estado_respaldo'
        ]
