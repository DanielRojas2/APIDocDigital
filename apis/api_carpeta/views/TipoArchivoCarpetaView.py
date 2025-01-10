from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloTipoArchivoCarpeta import ModeloTipoArchivoCarpeta
from ..serializers.TipoArchivoCarpetaSerializer import TipoArchivoCarpetaSerializer

class TipoArchivoCarpetaView(viewsets.ModelViewSet):
    queryset = ModeloTipoArchivoCarpeta.objects.all()
    serializer_class = TipoArchivoCarpetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
