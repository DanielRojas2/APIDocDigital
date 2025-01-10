from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloModalidadDespacho import ModeloModalidadDespacho
from ..serializers.ModalidadDespachoSerializer import ModalidadDespachoSerializer

class ModalidadDespachoView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloModalidadDespacho.objects.all()
    serializer_class = ModalidadDespachoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
