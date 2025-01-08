from rest_framework import generics
from ..models.ModeloClasificacionCarpeta import ModeloClasificacionCarpeta
from ..serializers.ClasificacionCarpetaSerializer import ClasificacionCarpetaSerializer

class ClasificacionCarpetaList(generics.ListAPIView):
    queryset = ModeloClasificacionCarpeta.objects.all()
    serializer_class = ClasificacionCarpetaSerializer
