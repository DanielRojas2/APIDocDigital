from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloPersonalAgencia import ModeloPersonalAgencia
from ..serializers.PersonalAgenciaSerializer import PersonalAgenciaSerializer

class PersonalAgenciaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloPersonalAgencia.objects.all()
    serializer_class = PersonalAgenciaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
