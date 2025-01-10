from rest_framework import serializers
from rest_framework.reverse import reverse
from ..models.ModeloCarpeta import ModeloCarpeta
from ...api_datoscarpeta.serializers import (
    AduanaDespachoSerializer, CanalAperturaSerializer, ClasificacionCarpetaSerializer,
    ImportadorSerializer, MercaderiaSerializer, ModalidadDespachoSerializer
)
from .PersonalCarpetaSerializer import PersonalAsignadoSerializer
from .TipoArchivoCarpetaSerializer import TipoArchivoCarpetaDetalleSerializer

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
    detalle_url = serializers.SerializerMethodField()

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
            'personal_asignado',
            'detalle_url'
        ]
    
    def get_personal_asignado(self, obj):
        from ..models.ModeloPersonalCarpeta import ModeloPersonalCarpeta
        personal = ModeloPersonalCarpeta.objects.filter(carpeta_asignada=obj)
        return PersonalAsignadoSerializer(personal, many=True).data
    
    def get_detalle_url(self, obj):
        request = self.context.get('request')
        if request:
            return reverse(
                'detalle-carpeta-detail',
                kwargs={'pk':obj.pk},
                request=request
            )
        return None

class CarpetaDetalleSerializer(serializers.ModelSerializer):
    tipos_archivo = TipoArchivoCarpetaDetalleSerializer(
        source='tipoarchivo_carpeta_set',
        many=True,
        read_only=True
    )
    class Meta:
        model = ModeloCarpeta
        fields = [
            'codigo_interno',
            'nro_dim',
            'tipos_archivo'
        ]
