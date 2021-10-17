"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserViewSet
from todo.views import ToDoViewSet, ProjectViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt  # не проверять наличие кукис в запросе

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo_app",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="shtyrov89@gmail.com"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('api/', include(router.urls))
]
