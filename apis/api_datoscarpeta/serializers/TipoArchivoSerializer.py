from rest_framework import serializers
from ..models.ModeloTipoArchivo import ModeloTipoArchivo

class TipoArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloTipoArchivo
        fields = '__all__'
