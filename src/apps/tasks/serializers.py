
from rest_framework import serializers
from .models import Tasks
from django.contrib.auth.models import User

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        # fileds = ["id" , "title" , "description"]


class UserSerializer(serializers.ModelSerializer):
    assigned_tasks = TasksSerializer(many= True, read_only=True)
    created_tasks = TasksSerializer(many= True , read_only=True)
    class Meta:
        model = User
        fields = '__all__'