from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TasksViewSet


router = SimpleRouter()
router.register('tasks' , TasksViewSet, basename='taks')

urlpatterns = [] + router.urls

