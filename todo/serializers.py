from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedRelatedField
from .models import Project
from .models import ToDo


class ProjectSerializer(ModelSerializer):
    superuser = HyperlinkedIdentityField(view_name='user-detail')
    users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    project = HyperlinkedIdentityField(view_name='project-detail')
    user = HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = ToDo
        fields = '__all__'
        # exclude = ('is_active',)
