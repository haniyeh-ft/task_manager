from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..tasks.serializers import TasksSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    assigned_tasks = TasksSerializer(many=True, read_only=True)
    created_tasks = TasksSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user