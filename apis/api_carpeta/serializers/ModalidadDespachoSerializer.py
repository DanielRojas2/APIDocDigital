from rest_framework import serializers
from ..models.ModeloModalidadDespacho import ModeloModalidadDespacho

class ModalidadDespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloModalidadDespacho
        fields = '__all__'
