from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TasksViewSet, UserViewSet


router = SimpleRouter()
router.register('tasks' , TasksViewSet, basename='taks')
router.register('users' , UserViewSet, basename='users')
urlpatterns = [] + router.urls
# urlpatterns = [
# '' , include(router.urls)
# ] 
