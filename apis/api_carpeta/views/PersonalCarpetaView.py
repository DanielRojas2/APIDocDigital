from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloPersonalCarpeta import ModeloPersonalCarpeta
from ..serializers.PersonalCarpetaSerializer import PersonalCarpetaSerializer

class PersonalCarpetaView(viewsets.ModelViewSet):
    queryset = ModeloPersonalCarpeta.objects.all()
    serializer_class = PersonalCarpetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
