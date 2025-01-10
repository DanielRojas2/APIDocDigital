from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloAduanaDespacho import ModeloAduanaDespacho
from ..serializers.AduanaDespachoSerializer import AduanaDespachoSerializer

class AduanaDespachoView(viewsets.ModelViewSet):
    queryset = ModeloAduanaDespacho.objects.all()
    serializer_class = AduanaDespachoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
