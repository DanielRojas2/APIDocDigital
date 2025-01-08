from rest_framework import viewsets
from ..models.ModeloMercaderia import ModeloMercaderia
from ..serializers.MercaderiaSerializer import MercaderiaSerializer

class MercaderiaView(viewsets.ModelViewSet):
    queryset = ModeloMercaderia.objects.all()
    serializer_class = MercaderiaSerializer
