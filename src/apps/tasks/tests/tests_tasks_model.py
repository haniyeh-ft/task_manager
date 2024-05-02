from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Task

User = get_user_model()

class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="09011231234",username='testuser', password='password')
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            created_by=self.user,
            priority=1
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task')
        self.assertEqual(self.task.status, 'pending')
        self.assertEqual(self.task.created_by, self.user)
        self.assertEqual(self.task.priority, 1)

    def test_task_str_method(self):
        expected_str = f"{self.task.title} - {self.task.status}"
        self.assertEqual(str(self.task), expected_str)

    def test_assigned_to_field(self):
        # Add users to the assigned_to field
        assigned_user1 = User.objects.create_user(phone_number="09011231235",username='assigned_to_user1', password='password')
        assigned_user2 = User.objects.create_user(phone_number="09011231236",username='assigned_user2', password='password')
        self.task.assigned_to.add(assigned_user1)
        self.task.assigned_to.add(assigned_user2)
        
        # Check if users are correctly added to assigned_to field
        self.assertIn(assigned_user1, self.task.assigned_to.all())
        self.assertIn(assigned_user2, self.task.assigned_to.all())

    def test_status_choices(self):
        # Check if the status field only accepts choices defined in STATUS_CHOICES
        valid_choices = ['pending', 'paused', 'archived', 'on_hold', 'in_progress', 'completed']
        invalid_choice = 'invalid_status'
        self.assertTrue(self.task.status in valid_choices)
        self.assertNotEqual(self.task.status, invalid_choice)

    def test_priority_choices(self):
        # Check if the priority field only accepts choices defined in PRIORITY_CHOICES
        valid_choices = [1, 2, 3]
        invalid_choice = 4
        self.assertTrue(self.task.priority in [choice[0] for choice in Task.PRIORITY_CHOICES])
        self.assertNotEqual(self.task.priority, invalid_choice)

