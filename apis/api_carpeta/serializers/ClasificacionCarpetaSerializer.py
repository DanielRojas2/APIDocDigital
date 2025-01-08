from rest_framework import serializers
from ..models.ModeloClasificacionCarpeta import ModeloClasificacionCarpeta

class ClasificacionCarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloClasificacionCarpeta
        fields = '__all__'
