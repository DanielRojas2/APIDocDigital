from rest_framework import viewsets
from ..models.ModeloTipoArchivo import ModeloTipoArchivo
from ..serializers.TipoArchivoSerializer import TipoArchivoSerializer

class TipoArchivoView(viewsets.ModelViewSet):
    queryset = ModeloTipoArchivo.objects.all()
    serializer_class = TipoArchivoSerializer
