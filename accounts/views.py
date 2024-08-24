from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import RegisterUserSerializer, LoginUserSerializer
from config.constants import Decision


class AuthenticateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        decision = request.data.get('decision')
        if decision not in [Decision.LOGIN, Decision.REGISTER]:
            return Response(data={'error': 'Invalid decision value'}, status=status.HTTP_400_BAD_REQUEST)

        if decision == Decision.LOGIN:
            return self._handle_login(request)
        elif decision == Decision.REGISTER:
            return self._handle_register(request)

    def _handle_login(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validate(request.data)
            refresh = RefreshToken.for_user(user)
            return Response(data={'refresh': str(refresh)}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _handle_register(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(data={'refresh': str(refresh)}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
