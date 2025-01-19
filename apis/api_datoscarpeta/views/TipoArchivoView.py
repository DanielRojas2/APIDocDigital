from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloTipoArchivo import ModeloTipoArchivo
from ..serializers.TipoArchivoSerializer import TipoArchivoSerializer

class TipoArchivoView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloTipoArchivo.objects.all()
    serializer_class = TipoArchivoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
