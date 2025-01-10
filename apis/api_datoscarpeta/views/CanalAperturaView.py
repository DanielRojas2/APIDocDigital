from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloCanalApertura import ModeloCanalApertura
from ..serializers.CanalAperturaSerializer import CanalAperturaSerializer

class CanalAperturaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloCanalApertura.objects.all()
    serializer_class = CanalAperturaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
