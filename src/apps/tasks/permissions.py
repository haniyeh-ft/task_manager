from rest_framework import permissions


class IsTaskCreator(permissions.BasePermission):
    """
    Custom permission to only allow the user who created a task to modify or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsAssignedUser(permissions.BasePermission):
    """
    Custom permission to only allow the assigned user to modify or delete a task.
    """

    def has_object_permission(self, request, view, obj):
        return True if request.user in obj.assigned_to.all() else False
