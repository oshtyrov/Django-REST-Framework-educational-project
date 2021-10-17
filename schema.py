import graphene
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    all_todos = graphene.List(ToDoType)

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    todos_by_project_name = graphene.List(ToDoType, name=graphene.String(required=False))

    # По названию проекта получаем все связанные с ним todo, пользователей

    def resolve_todos_by_project_name(self, info, name=None):
        todos = ToDo.objects.all()
        if name:
            todos = todos.filter(project__name=name)
        return todos

    projects_by_user_id = graphene.List(ProjectType, user_id=graphene.Int(required=False))

    # По id автора получаем все проекты, в которых он участвует

    def resolve_projects_by_user_id(self, info, user_id=None):
        projects = Project.objects.all()
        if user_id:
            projects = projects.filter(users__id=user_id)
        return projects


schema = graphene.Schema(query=Query)
