from rest_framework import viewsets
from ..models.ModeloClasificacionCarpeta import ModeloClasificacionCarpeta
from ..serializers.ClasificacionCarpetaSerializer import ClasificacionCarpetaSerializer

class ClasificacionCarpetaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloClasificacionCarpeta.objects.all()
    serializer_class = ClasificacionCarpetaSerializer
