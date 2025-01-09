from rest_framework import viewsets
from ..models.ModeloCarpeta import ModeloCarpeta
from ..serializers.CarpetaSerializer import CarpetaSerializer, ReporteCarpetaSerializer

class CarpetaView(viewsets.ModelViewSet):
    queryset = ModeloCarpeta.objects.all()
    serializer_class = CarpetaSerializer

class ReporteCarpetaView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReporteCarpetaSerializer
    queryset = ModeloCarpeta.objects.all()
