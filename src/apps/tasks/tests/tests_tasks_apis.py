from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from ..models import Task

User = get_user_model()


class TasksAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="09011231234", username="testuser", password="password"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        # Task data for POST request
        self.task_data = {
            "title": "test",
            "description": "string",
            "status": "pending",
            "priority": 1,
            "created_by": self.user.pk
        }

        # Create Task object with created_by field set to the User instance
        self.task = Task.objects.create(
            title="test",
            description="string",
            status="pending",
            priority=1,
            created_by=self.user
        )


    def test_tasks_get_api(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tasks_post_api(self):
        response = self.client.post("/tasks/", data=self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_tasks_get_by_id_api(self):
        response = self.client.get(f"/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task_data["title"])

    def test_tasks_update__with_permission_error(self):
        updated_title = "Updated Task"
        response = self.client.put(
            f"/tasks/{self.task.id}/", data={"title": updated_title}
        )
        print("**** res " , response.data)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)


    def test_tasks_update__without_permission_error(self):
        user_assigned_to = User.objects.get(pk=self.user.id)
        self.task.assigned_to.set([user_assigned_to])
        updated_title = "Updated Task"
        response = self.client.patch(
                    f"/tasks/{self.task.id}/", data={"title": updated_title}
                )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task.id).title, updated_title)


    def test_tasks_delete_by_id_api(self):
        user_assigned_to = User.objects.get(pk=self.user.id)
        self.task.assigned_to.set([user_assigned_to])

        response = self.client.delete(f"/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
