from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class TelegramApiTestCase(APITestCase):
    def setUp(self):
        """Set up initial test data"""
        self.user = User.objects.create(
            telegram_id=34,  # Ensure ID matches the test case
            username="test_user",
            first_name="John",
            last_name="Doe"
        )

        self.base_url = "/api/auth"

    def test_create_user_via_telegram_api(self):
        """Test user registration via Telegram API"""
        new_user_data = {
            "first_name": "Alice",
            "last_name": "Smith",
            "username": "new_user",
            "telegram_id": 9924567654,
        }
        response = self.client.post(f"{self.base_url}/tg", new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["telegram_id"], new_user_data["telegram_id"])

    def test_create_user_invalid_data(self):
        """Test invalid user creation"""
        invalid_data = {"telegram_id": "incomplete_user"}  # Missing telegram_id
        response = self.client.post(f"{self.base_url}/tg", invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("telegram_id", response.data)  # Check for validation error

    def test_get_all_users(self):
        """Test retrieving all users"""
        response = self.client.get(f"{self.base_url}/users")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # Ensure at least one user exists

    def test_get_specific_user(self):
        """Test fetching a user by telegram_id"""
        response = self.client.get(f"{self.base_url}/users/{self.user.telegram_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["telegram_id"], self.user.telegram_id)

    def test_get_non_existent_user(self):
        """Test retrieving a user that does not exist"""
        response = self.client.get(f"{self.base_url}/users/99999999")  # Invalid telegram_id
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
# import pytest
# from django.urls import reverse
# from rest_framework import status
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# @pytest.fixture
# def create_user(db):
#     """Test uchun foydalanuvchi yaratish"""  # noqa
#     return User.objects.create(
#         telegram_id=34,  # Test case bilan mos kelishi kerak # noqa
#         username="test_user",
#         first_name="John",
#         last_name="Doe"
#     )
#
#
# @pytest.fixture
# def api_client():
#     """Django test client uchun fixture"""  # noqa
#     from rest_framework.test import APIClient
#     return APIClient()
#
#
# @pytest.mark.django_db
# def test_create_user_via_telegram_api(api_client):
#     """Telegram API orqali foydalanuvchi ro‘yxatdan o‘tishini test qilish"""  # noqa
#     new_user_data = {
#         "first_name": "Alice",
#         "last_name": "Smith",
#         "username": "new_user",
#         "telegram_id": 9924567654,
#     }
#     url = reverse("telegram-auth")  # `urls.py` da nomlangan `path` kerak # noqa
#     response = api_client.post(url, new_user_data)
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data["telegram_id"] == new_user_data["telegram_id"]
#
#
# @pytest.mark.django_db
# def test_create_user_invalid_data(api_client):
#     """Noto‘g‘ri foydalanuvchi ma’lumotlarini tekshirish"""  # noqa
#     invalid_data = {"telegram_id": "incomplete_user"}  # `telegram_id` yetishmaydi # noqa
#     url = reverse("telegram-auth")
#     response = api_client.post(url, invalid_data)
#
#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#     assert "telegram_id" in response.data  # Validatsiya xatosi borligini tekshiramiz # noqa
#
#
# @pytest.mark.django_db
# def test_get_all_users(api_client, create_user):
#     """Barcha foydalanuvchilar ro‘yxatini olishni test qilish"""  # noqa
#     url = reverse("telegram-user-list")
#     response = api_client.get(url)
#
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) >= 1  # Kamida bitta foydalanuvchi borligini tekshiramiz # noqa
#
#
# @pytest.mark.django_db
# def test_get_specific_user(api_client, create_user):
#     """Telegram ID orqali ma’lum bir foydalanuvchini olishni test qilish"""  # noqa
#     url = reverse("telegram-user-detail", kwargs={"pk": create_user.telegram_id})
#     response = api_client.get(url)
#
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data["telegram_id"] == create_user.telegram_id
#
#
# @pytest.mark.django_db
# def test_get_non_existent_user(api_client):
#     """Mavjud bo‘lmagan foydalanuvchini olish testi"""  # noqa
#     url = reverse("telegram-user-detail", kwargs={"pk": 99999999})  # Yaroqsiz `telegram_id` # noqa
#     response = api_client.get(url)
#
#     assert response.status_code == status.HTTP_404_NOT_FOUND