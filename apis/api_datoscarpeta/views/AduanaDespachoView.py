from rest_framework import viewsets
from ..models.ModeloAduanaDespacho import ModeloAduanaDespacho
from ..serializers.AduanaDespachoSerializer import AduanaDespachoSerializer

class ModeloAduanaDespachoView(viewsets.ModelViewSet):
    queryset = ModeloAduanaDespacho.objects.all()
    serializer_class = AduanaDespachoSerializer
