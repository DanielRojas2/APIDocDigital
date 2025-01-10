from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloDocumentoSoporte import ModeloDocumentoSoporte
from ..serializers.DocumentoSoporteSerializer import DocumentoSoporteSerializer

class DocumentoSoporteView(viewsets.ModelViewSet):
    queryset = ModeloDocumentoSoporte.objects.all()
    serializer_class = DocumentoSoporteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
