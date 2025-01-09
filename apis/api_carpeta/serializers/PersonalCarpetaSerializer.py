from rest_framework import serializers
from ..models.ModeloPersonalCarpeta import ModeloPersonalCarpeta

class PersonalCarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloPersonalCarpeta
        fields = [
            'id',
            'personal_asignado',
            'carpeta_asignada',
            'rol_asignado'
        ]
