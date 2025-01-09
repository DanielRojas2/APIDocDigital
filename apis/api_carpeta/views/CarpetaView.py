from rest_framework import viewsets
from ..models.ModeloCarpeta import ModeloCarpeta
from ..serializers.CarpetaSerializer import CarpetaSerializer

class CarpetaView(viewsets.ModelViewSet):
    queryset = ModeloCarpeta.objects.all()
    serializer_class = CarpetaSerializer
