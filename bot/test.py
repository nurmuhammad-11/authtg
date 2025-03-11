import unittest
import requests
import config

class TestAPI(unittest.TestCase):
    def test_auth(self):
        data = {"telegram_id": "123456"}
        response = requests.post(config.AUTH_API, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

    def test_get_all_users(self):
        response = requests.get(config.USER_API)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_get_user_by_id(self):
        user_id = 1
        response = requests.get(f"{config.GET_USER}{user_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

if __name__ == "__main__":
    unittest.main()
