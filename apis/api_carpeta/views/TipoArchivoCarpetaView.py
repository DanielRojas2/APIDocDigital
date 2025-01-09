from rest_framework import viewsets
from ..models.ModeloTipoArchivoCarpeta import ModeloTipoArchivoCarpeta
from ..serializers.TipoArchivoCarpetaSerializer import TipoArchivoCarpetaSerializer

class TipoArchivoCarpetaView(viewsets.ModelViewSet):
    queryset = ModeloTipoArchivoCarpeta.objects.all()
    serializer_class = TipoArchivoCarpetaSerializer
