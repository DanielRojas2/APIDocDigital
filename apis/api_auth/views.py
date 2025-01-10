from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            context = {
                'status': True,
                'content': str(refresh.access_token)
            }
        else:
            context = {
                'status': False,
                'content': 'Credenciales no válidas'
            }
        return Response(context)
