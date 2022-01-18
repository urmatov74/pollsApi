from django.contrib import auth
from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.auth.serializers import UserRegisterSerializer, LoginSerializer


# Create your views here.


class UserRegisterView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializers.ValidationError, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        # if request.user.is_authenticated:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # else:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        user.auth_token.delete()
        auth.logout(request)
