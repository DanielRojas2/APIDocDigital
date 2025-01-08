from rest_framework import viewsets
from ..models.ModeloImportador import ModeloImportador
from ..serializers.ImportadorSerializer import ImportadorSerializer

class ImportadorView(viewsets.ModelViewSet):
    queryset = ModeloImportador.objects.all()
    serializer_class = ImportadorSerializer
