from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloClasificacionCarpeta import ModeloClasificacionCarpeta
from ..serializers.ClasificacionCarpetaSerializer import ClasificacionCarpetaSerializer

class ClasificacionCarpetaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloClasificacionCarpeta.objects.all()
    serializer_class = ClasificacionCarpetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
