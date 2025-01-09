from rest_framework import serializers
from ..models.ModeloPersonalCarpeta import ModeloPersonalCarpeta

class PersonalCarpetaSerializer(serializers.ModelSerializer):
    personal_asignado_nombre = serializers.CharField(
        source='personal_asignado.nombre_personal'
    )
    class Meta:
        model = ModeloPersonalCarpeta
        fields = [
            'id',
            'personal_asignado_nombre',
            'carpeta_asignada',
            'rol_asignado'
        ]
