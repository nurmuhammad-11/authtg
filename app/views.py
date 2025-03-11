from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from app.serializers import UserSerializer
from app.models import User
from drf_spectacular.utils import extend_schema


class TelegramApiView(APIView):
    serializer_class = UserSerializer

    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer},
        tags=['Telegram Auth'])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TelegramUserListAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class TelegramUserDetailAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request, pk):
        user = get_object_or_404(User, telegram_id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)