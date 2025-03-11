from django.urls import path

from app.views import TelegramApiView, TelegramUserListAPIView, TelegramUserDetailAPIView

urlpatterns = [
    path('auth/tg', TelegramApiView.as_view()),
    path('auth/users', TelegramUserListAPIView.as_view()),
    path('auth/users/<int:pk>', TelegramUserDetailAPIView.as_view()),
]
