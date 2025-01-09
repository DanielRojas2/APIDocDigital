from rest_framework import serializers
from ..models.ModeloCarpeta import ModeloCarpeta
from ...api_datoscarpeta.serializers import (
    AduanaDespachoSerializer, CanalAperturaSerializer, ClasificacionCarpetaSerializer,
    ImportadorSerializer, MercaderiaSerializer, ModalidadDespachoSerializer
)
from .PersonalCarpetaSerializer import PersonalCarpetaSerializer

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

class ReporteCarpetaSerializer(serializers.ModelSerializer):
    canal = CanalAperturaSerializer.CanalAperturaSerializer()
    modalidad_despacho = ModalidadDespachoSerializer.ModalidadDespachoSerializer()
    importador = ImportadorSerializer.ImportadorSerializer()
    aduana_despacho = AduanaDespachoSerializer.AduanaDespachoSerializer()
    clasificacion_carpeta = ClasificacionCarpetaSerializer.ClasificacionCarpetaSerializer()
    mercaderia = MercaderiaSerializer.MercaderiaSerializer()
    personal_asignado = serializers.SerializerMethodField()

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
            'mercaderia',
            'personal_asignado'
        ]
    
    def get_personal_asignado(self, obj):
        from ..models.ModeloPersonalCarpeta import ModeloPersonalCarpeta
        personal = ModeloPersonalCarpeta.objects.filter(carpeta_asignada=obj)
        return PersonalCarpetaSerializer(personal, many=True).data
