import json
import sys

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Project, ToDo

sys.path.append("/Django_REST_Framework/library/users/")
from users.models import User


class TestProjectViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/projects/{project.id}/', {"name": "test_project_1",
                                                                    "repository": "https://www.google.com.ua/?hl=ru",
                                                                    "id": 1, "users": project.users})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'test_project_1')

    def test_get_detail(self):
        project = mixer.blend(Project, name='test_project_2')
        response = self.client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_project = json.loads(response.content)
        self.assertEqual(response_project['name'], 'test_project_2')


class TestToDoViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


