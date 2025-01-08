from rest_framework import serializers
from ..models.ModeloMercaderia import ModeloMercaderia

class MercaderiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloMercaderia
        fields = '__all__'
