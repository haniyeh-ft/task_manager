from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    # set index and tell the reason
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paused", "Paused"),
        ("archived", "Archived"),
        ("on_hold", "On Hold"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    )
    PRIORITY_CHOICES = ((1, "Low"), (2, "Medium"), (3, "High"))
    title = models.CharField(max_length=300, blank=False)  # index
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    assigned_to = models.ManyToManyField(
        User, related_name="assigned_tasks", null=True, blank=True
    )
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="created_tasks"
    )
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)

    def __str__(self) -> str:
        return f"{self.title} - {self.status}"
