from rest_framework import viewsets
from .models import Task
from .serializers import TasksSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
