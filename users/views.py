from rest_framework import viewsets
from rest_framework import mixins
# from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer, UserSerializerBase


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # renderer_classes = [JSONRenderer]

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return UserSerializer
        return UserSerializerBase


