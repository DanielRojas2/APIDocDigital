from rest_framework import generics
from ..models.ModeloModalidadDespacho import ModeloModalidadDespacho
from ..serializers.ModalidadDespachoSerializer import ModalidadDespachoSerializer

class ModalidadDespachoList(generics.ListAPIView):
    queryset = ModeloModalidadDespacho.objects.all()
    serializer_class = ModalidadDespachoSerializer
