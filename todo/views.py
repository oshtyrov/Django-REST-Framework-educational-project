from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, ToDoSerializer, ProjectSerializerBase, ToDoSerializerBase
from .models import Project, ToDo
from rest_framework.response import Response


class ProjectPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectPagination

    def get_queryset(self):
        projects = Project.objects.all()
        name = self.request.query_params.get('name', '')
        if name:
            projects = projects.filter(name__contains=name)
        return projects

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectSerializer
        return ProjectSerializerBase


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    filter_fields = ['project']
    pagination_class = ToDoPagination

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        return Response(data='delete success')

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ToDoSerializer
        return ToDoSerializerBase
