from rest_framework import viewsets
from ..models.ModeloModalidadDespacho import ModeloModalidadDespacho
from ..serializers.ModalidadDespachoSerializer import ModalidadDespachoSerializer

class ModalidadDespachoView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloModalidadDespacho.objects.all()
    serializer_class = ModalidadDespachoSerializer
