from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloImportador import ModeloImportador
from ..serializers.ImportadorSerializer import ImportadorSerializer

class ImportadorView(viewsets.ModelViewSet):
    queryset = ModeloImportador.objects.all()
    serializer_class = ImportadorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
