# from mixer.backend.django import mixer
# from rest_framework import status
# from rest_framework.test import APITestCase
# import json
# from .models import Project, ToDo
# from ..users.models import User
#
#
# class TestProjectViewSet(APITestCase):
#
#     def test_get_list(self):
#         response = self.client.get('/api/projects/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_edit_mixer(self):
#         project = mixer.blend(Project)
#         admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
#         self.client.login(username='admin', password='admin123456')
#         response = self.client.put(f'/api/projects/{project.id}/', {'name': 'test_project_1', 'users': project.users})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         project = Project.objects.get(id=project.id)
#         self.assertEqual(project.name, 'test_project_1')
#
#     def test_get_detail(self):
#         project = mixer.blend(Project, name='test_project_2')
#         response = self.client.get(f'/api/projects/{project.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         response_project = json.loads(response.content)
#         self.assertEqual(response_project['name'], 'test_project_2')
#
#
# class TestToDoViewSet(APITestCase):
#
#     def test_get_list(self):
#         response = self.client.get('/api/todos/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_detail_todo(self):
#         todo = mixer.blend(ToDo, user__name='test_user_1')
#         response = self.client.get(f'/api/todos/{todo.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         response_todo = json.loads(response.content)
#         self.assertEqual(response_todo['user']['name'], 'test_user_1')
