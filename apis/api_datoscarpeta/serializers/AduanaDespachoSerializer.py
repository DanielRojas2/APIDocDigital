from rest_framework import serializers
from ..models.ModeloAduanaDespacho import ModeloAduanaDespacho

class AduanaDespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloAduanaDespacho
        fields = '__all__'
