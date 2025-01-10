from rest_framework import serializers
from ..models.ModeloTipoArchivoCarpeta import ModeloTipoArchivoCarpeta
from .DocumentoSoporteSerializer import DocumentoSoporteSerializer

class TipoArchivoCarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloTipoArchivoCarpeta
        fields = ['id', 'carpeta', 'tipo_archivo']

class TipoArchivoCarpetaDetalleSerializer(serializers.ModelSerializer):
    tipo_archivo = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tipo_archivo'
    )
    documentos_soporte = DocumentoSoporteSerializer(
        source='documento_soporte',
        read_only=True
    )

    class Meta:
        model = ModeloTipoArchivoCarpeta
        fields = ['id', 'tipo_archivo', 'documentos_soporte', 'creado']
