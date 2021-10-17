from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedRelatedField
from .models import Project
from .models import ToDo
from users.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    # superuser = HyperlinkedIdentityField(view_name='user-detail')
    # users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializerBase(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    # project = HyperlinkedIdentityField(view_name='project-detail')
    # user = HyperlinkedIdentityField(view_name='user-detail')
    project = StringRelatedField()
    user = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
        # exclude = ('is_active',)


class ToDoSerializerBase(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
