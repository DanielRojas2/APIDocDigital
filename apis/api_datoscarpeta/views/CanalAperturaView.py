from rest_framework import viewsets
from ..models.ModeloCanalApertura import ModeloCanalApertura
from ..serializers.CanalAperturaSerializer import CanalAperturaSerializer

class CanalAperturaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloCanalApertura.objects.all()
    serializer_class = CanalAperturaSerializer
