from rest_framework import viewsets
from ..models.ModeloPersonalCarpeta import ModeloPersonalCarpeta
from ..serializers.PersonalCarpetaSerializer import PersonalCarpetaSerializer

class PersonalCarpetaView(viewsets.ModelViewSet):
    queryset = ModeloPersonalCarpeta.objects.all()
    serializer_class = PersonalCarpetaSerializer
