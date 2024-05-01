from .models import Task
from .serializers import TasksSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "creation_date", "priority" , "status"]
