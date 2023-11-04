from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterUserSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        user_serializer = RegisterUserSerializer(data=request.data)
        if user_serializer.is_valid():
            new_user = user_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
