from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloMercaderia import ModeloMercaderia
from ..serializers.MercaderiaSerializer import MercaderiaSerializer

class MercaderiaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloMercaderia.objects.all()
    serializer_class = MercaderiaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
