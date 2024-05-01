from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        # fileds = ["id" , "title" , "description"]


class UserSerializer(serializers.ModelSerializer):
    assigned_tasks = TasksSerializer(many=True, read_only=True)
    created_tasks = TasksSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
