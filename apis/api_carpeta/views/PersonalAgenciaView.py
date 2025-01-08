from rest_framework import viewsets
from ..models.ModeloPersonalAgencia import ModeloPersonalAgencia
from ..serializers.PersonalAgenciaSerializer import PersonalAgenciaSerializer

class PersonalAgenciaView(viewsets.ModelViewSet):
    queryset = ModeloPersonalAgencia.objects.all()
    serializer_class = PersonalAgenciaSerializer
