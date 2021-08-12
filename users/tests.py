import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import User


class TestUserViewSetTestCase(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/', format='json')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        user = User.objects.create(username='Васятко', phone="+700000000")
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserViewSetAPITestCase(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        user = mixer.blend(User)
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_unauthorized_user(self):
        user = mixer.blend(User)
        response = self.client.put(f'/api/users/{user.id}/',
                                   {"username": "Васятко", "phone": "+380631591111", "password": "qwert1234",
                                    "email": "qwer@gmail.com"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = mixer.blend(User)
        admin = User.objects.create_superuser(username='admin', email='admin@admin.com',
                                              password='admin123456', phone='+380631591111')
        response = self.client.get(f'/api/users/{admin.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(admin.username, "admin")
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/users/{user.id}/',
                                   {"username": "Васятко", "phone": "+380631591111", "password": "qwert1234",
                                    "email": "qwer@gmail.com"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, "Васятко")





