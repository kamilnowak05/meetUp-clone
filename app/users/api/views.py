from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.settings import api_settings

from users.api.serializers import UserSerializer, AuthTokenSerializer
from users.models import User


class CreateUserView(generics.CreateAPIView):
    """Create new user in the  system"""
    serializer_class = UserSerializer


class LoginUserView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# class LogoutUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = AuthTokenSerializer

#     def post(self, request):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']

#         Token.objects.filter(user=user).delete()
#         token, created = Token.objects.create(user=user)

#         return Response({'token': token.key})


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrive and return authentication user"""
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
