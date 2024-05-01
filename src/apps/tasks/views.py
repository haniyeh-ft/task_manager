from rest_framework import viewsets
from .models import Tasks
from .serializers import TasksSerializer, UserSerializer
from django.contrib.auth.models import User


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
