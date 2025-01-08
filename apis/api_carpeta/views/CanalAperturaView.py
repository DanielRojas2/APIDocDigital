from rest_framework import generics
from ..models.ModeloCanalApertura import ModeloCanalApertura
from ..serializers.CanalAperturaSerializer import CanalAperturaSerializer

class CanalAperturaListView(generics.ListAPIView):
    queryset = ModeloCanalApertura.objects.all()
    serializer_class = CanalAperturaSerializer
