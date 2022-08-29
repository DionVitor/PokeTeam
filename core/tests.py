from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from core.app.api.views.user_view import UserViewSet
from users.models import User


class GetUserTestCase(TestCase):
    user_view = UserViewSet.as_view({"get": "retrieve"})

    def test_get_user(self):
        user_data = {
            "username": "Username",
            "email": "test@test.com",
            "password": "abc"
        }

        user = User.objects.create_user(**user_data)

        factory = APIRequestFactory()
        request = factory.get(f"/users/{user.id}", format="json")
        force_authenticate(request, User.objects.get(username=user_data.get("username")))
        api_response = UserViewSet.as_view({"get": "retrieve"})(request, pk=f"{user.id}")

        user_columns = {"username", "email", "first_name", "last_name"}
        user_from_api_fields = {key for key in api_response.data}

        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(user_from_api_fields - user_columns, set())

    def test_get_user_with_invalid_credentials(self):
        user_data = {
            "username": "Username",
            "email": "test@test.com",
            "password": "abc"
        }

        user = User.objects.create_user(**user_data)

        factory = APIRequestFactory()
        request = factory.get(f"/users/{user.id}", format="json")
        api_response = UserViewSet.as_view({"get": "retrieve"})(request, pk=f"{user.id}")

        self.assertEqual(api_response.status_code, 403)

    def test_get_user_and_not_found_user(self):
        user_data = {
            "username": "Username",
            "email": "test@test.com",
            "password": "abc"
        }

        User.objects.create_user(**user_data)

        factory = APIRequestFactory()
        request = factory.get("/users/10", format="json")
        force_authenticate(request, User.objects.get(username=user_data.get("username")))
        api_response = UserViewSet.as_view({"get": "retrieve"})(request, pk="10")

        self.assertEqual(api_response.status_code, 404)

    def test_get_user_not_expose_credentials(self):
        user_data = {
            "username": "Username",
            "email": "test@test.com",
            "password": "abc"
        }

        User.objects.create_user(**user_data)

        factory = APIRequestFactory()
        request = factory.get("/users/1", format="json")
        force_authenticate(request, User.objects.get(username=user_data.get("username")))
        api_response = UserViewSet.as_view({"get": "retrieve"})(request, pk="1")

        self.assertFalse(api_response.data.get("password", False))
