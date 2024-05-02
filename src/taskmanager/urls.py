from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from apps.tasks.views import TasksViewSet
from apps.users.views import UsersViewSet

# Create a router
router = DefaultRouter()
router.register(r"tasks", TasksViewSet, basename="tasks")
router.register(r"users", UsersViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", include(router.urls)),
]
