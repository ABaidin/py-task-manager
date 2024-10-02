from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from task_manager_app.models import TaskType, Task, Position, Employee


class TaskManagerViewsTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Feature Development")
        self.position = Position.objects.create(name="Developer")
        self.employee = Employee.objects.create_user(
            username="john_doe",
            password="password123",
            position=self.position
        )
        self.task = Task.objects.create(
            name="Implement Payment Gateway",
            description="Integrate Stripe API",
            deadline=timezone.now(),
            is_completed=False,
            task_type=self.task_type,
            priority=Task.Priority.HIGH,
        )
        self.task.assigned_to.add(self.employee)
        self.client.force_login(self.employee)

    def test_task_list_view_uses_correct_template(self):
        response = self.client.get(reverse('tasks:tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_manager/task_list.html')

    def test_task_update(self):
        data = {
            'name': 'Updated Task',
            'description': 'Updated Description',
            'deadline': timezone.now(),
            'is_completed': True,
            'task_type': self.task_type.id,
            'priority': Task.Priority.MEDIUM,
            'assigned_to': [self.employee.id]
        }
        self.client.post(reverse(
            'tasks:task-update', args=[self.task.id]), data=data
        )
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.name, "Updated Task")
        self.assertEqual(updated_task.is_completed, True)

    def test_task_delete(self):
        self.client.post(reverse('tasks:task-delete', args=[self.task.id]))
        tasks = Task.objects.filter(id=self.task.id)
        self.assertEqual(tasks.count(), 0)
