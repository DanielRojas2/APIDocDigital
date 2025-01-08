from rest_framework import serializers
from ..models.ModeloPersonalAgencia import ModeloPersonalAgencia

class PersonalAgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloPersonalAgencia
        fields = [
            'id',
            'nombre_personal',
            'apellido_personal',
            'telefono_personal'
        ]
