from rest_framework import viewsets
from rest_framework import mixins
# from rest_framework.renderers import JSONRenderer
# from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer, UserSerializerV2


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    # renderer_classes = [JSONRenderer]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerV2
        return UserSerializer


