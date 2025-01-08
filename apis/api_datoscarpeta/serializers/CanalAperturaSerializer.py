from rest_framework import serializers
from ..models.ModeloCanalApertura import ModeloCanalApertura

class CanalAperturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloCanalApertura
        fields = ['id', 'tipo_canal']
