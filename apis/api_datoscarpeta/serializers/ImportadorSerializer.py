from rest_framework import serializers
from ..models.ModeloImportador import ModeloImportador

class ImportadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloImportador
        fields = [
            'id',
            'nombre_importador',
            'nit_importador',
            'tipo_importador'
        ]
