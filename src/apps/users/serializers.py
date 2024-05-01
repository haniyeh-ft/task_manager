from rest_framework import serializers

from django.contrib.auth import get_user_model
from ..tasks.serializers import TasksSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    assigned_tasks = TasksSerializer(many=True, read_only=True)
    created_tasks = TasksSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
