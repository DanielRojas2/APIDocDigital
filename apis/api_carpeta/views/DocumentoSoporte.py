from rest_framework import viewsets
from ..models.ModeloDocumentoSoporte import ModeloDocumentoSoporte
from ..serializers.DocumentoSoporteSerializer import DocumentoSoporteSerializer

class DocumentoSoporteView(viewsets.ModelViewSet):
    queryset = ModeloDocumentoSoporte.objects.all()
    serializer_class = DocumentoSoporteSerializer
