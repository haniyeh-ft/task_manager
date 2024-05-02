from rest_framework.routers import SimpleRouter

from .views import UsersViewSet

router = SimpleRouter()
router.register("", UsersViewSet, basename="users")

urlpatterns = [] + router.urls
