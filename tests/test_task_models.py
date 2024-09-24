from django.test import TestCase
from django.utils import timezone

from task_manager_app.models import TaskType, Position, Employee, Task


class TaskManagerModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.employee = Employee.objects.create_user(
            username="john_doe",
            password="password123",
            first_name="John",
            last_name="Doe",
            position=self.position
        )
        self.task = Task.objects.create(
            name="Fix login bug",
            description="Fix the issue where users can't log in.",
            deadline=timezone.now(),
            is_completed=False,
            task_type=self.task_type,
            priority=Task.Priority.URGENT,
        )
        self.task.assigned_to.add(self.employee)

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bug Fix")

    def test_employee_str(self):
        self.assertEqual(
            str(self.employee),
            f"{self.employee.position} "
            f"{self.employee.first_name} {self.employee.last_name}"
        )

    def test_employee_attributes(self):
        self.assertEqual(self.employee.username, "john_doe")
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.position, Position.objects.get(name="Developer"))
        self.assertTrue(self.employee.check_password("password123"))

    def test_task_str(self):
        self.assertEqual(str(self.task), "Fix login bug")

    def test_task_attributes(self):
        self.assertEqual(self.task.name, "Fix login bug")
        self.assertEqual(self.task.description, "Fix the issue where users can't log in.")
        self.assertEqual(self.task.is_completed, False)
        self.assertEqual(self.task.priority, Task.Priority.URGENT)
        self.assertEqual(self.task.task_type, self.task_type)
        self.assertIn(self.employee, self.task.assigned_to.all())
