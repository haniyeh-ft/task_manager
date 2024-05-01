from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = ['username']
