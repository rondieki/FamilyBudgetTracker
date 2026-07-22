from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "username": user.username,
            "email": user.email,
            "currency": user.preferred_currency
        })
