from rest_framework.routers import SimpleRouter

from .views import TasksViewSet

router = SimpleRouter()
router.register('' , TasksViewSet, basename='taks')

urlpatterns = [] + router.urls

