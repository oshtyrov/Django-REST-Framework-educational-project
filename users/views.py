from rest_framework import viewsets
from rest_framework import mixins
# from rest_framework.renderers import JSONRenderer
from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # renderer_classes = [JSONRenderer]
