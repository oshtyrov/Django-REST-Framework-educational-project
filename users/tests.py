import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import User


class TestUserViewSet(TestCase):

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

    def test_edit_admin(self):
        user = User.objects.create(username='Васятко', phone="+700000000")
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{user.id}/', {'username': 'Галина', 'phone': '+800000000'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, 'Галина')
        self.assertEqual(user.phone, '+800000000')
        client.logout()

    # def test_post_user(self):
    #     factory = APIRequestFactory()
    #     admin = User.objects.create_superuser('test', 'test@test.com', 'qwerty123456')
    #     # test_user = mixer.blend(User)
    #     # request = factory.post('/api/users/', {'results': [test_user]})
    #     request = factory.post('/api/users/', {
    #         "results": [
    #             {
    #                 "username": "111",
    #                 "first_name": "111",
    #                 "last_name": "111",
    #                 "email": "shtyrov89@gmail.com"
    #             }
    #         ]})
    #     force_authenticate(request, admin)
    #     view = UserViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
