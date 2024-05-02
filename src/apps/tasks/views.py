from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Task
from .permissions import IsAssignedUser
from .serializers import TasksSerializer



class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "creation_date", "priority", "status"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [
                IsAssignedUser(),
            ]

        return super().get_permissions()
