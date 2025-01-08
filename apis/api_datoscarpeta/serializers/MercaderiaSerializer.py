from rest_framework import serializers
from ..models.ModeloMercaderia import ModeloMercaderia

class MercaderiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloMercaderia
        fields = ['id', 'nombre_mercaderia']
