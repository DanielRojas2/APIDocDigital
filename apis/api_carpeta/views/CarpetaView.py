from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.ModeloCarpeta import ModeloCarpeta
from ..serializers.CarpetaSerializer import (
    CarpetaSerializer, ReporteCarpetaSerializer, CarpetaDetalleSerializer
)

class CarpetaView(viewsets.ModelViewSet):
    queryset = ModeloCarpeta.objects.all()
    serializer_class = CarpetaSerializer

class ReporteCarpetaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloCarpeta.objects.all()
    serializer_class = ReporteCarpetaSerializer

class DetalleCarpetaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloCarpeta.objects.prefetch_related(
        'tipoarchivo_carpeta_set__tipo_archivo',
        'tipoarchivo_carpeta_set__documento_soporte'
    )
    serializer_class = CarpetaDetalleSerializer
