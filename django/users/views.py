from rest_framework import generics
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model as User


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User().objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User().objects.all()
    serializer_class = UserSerializer
