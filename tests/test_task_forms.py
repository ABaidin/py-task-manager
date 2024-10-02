from django.test import TestCase
from django.utils import timezone

from django import forms
from task_manager_app.forms import TaskForm, TaskSearchForm
from task_manager_app.models import TaskType, Position, Employee, Task


class TaskFormTest(TestCase):

    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.position = Position.objects.create(name="Developer")
        self.employee = Employee.objects.create_user(
            username="john_doe",
            password="password123",
            position=self.position
        )

    def test_task_form_placeholders(self):
        form = TaskForm()
        self.assertEqual(form.fields['name'].label, "Name")
        self.assertEqual(form.fields['description'].widget.attrs.get('placeholder'),None)

    def test_valid_task_form(self):
        form_data = {
            'name': 'Fix login issue',
            'description': 'There is an issue with the login system',
            'deadline': timezone.now(),
            'is_completed': False,
            'task_type': self.task_type.id,
            'priority': Task.Priority.URGENT,
            'assigned_to': [self.employee.id]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_task_form(self):
        form_data = {
            'name': '',
            'description': 'Description here',
            'deadline': timezone.now(),
            'is_completed': False,
            'task_type': self.task_type.id,
            'priority': Task.Priority.URGENT,
            'assigned_to': [self.employee.id]
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

class TaskSearchFormTest(TestCase):

    def setUp(self):
        self.task_type1 = TaskType.objects.create(name="Bug Fix")
        self.task_type2 = TaskType.objects.create(name="Feature Development")

    def test_form_field_attributes(self):
        form = TaskSearchForm()

        self.assertEqual(form.fields['name'].widget.attrs['placeholder'], "Search by name...")
        self.assertEqual(form.fields['name'].widget.attrs['class'], "form-control")

        self.assertEqual(form.fields['task_type'].empty_label, "-- Filter by Task Type --")
        self.assertEqual(form.fields['task_type'].widget.attrs['class'], "form-select")

        self.assertIsInstance(form.fields['show_my_tasks'].widget, forms.CheckboxInput)
        self.assertEqual(form.fields['show_my_tasks'].label, "Show only my tasks")

    def test_valid_form(self):
        form_data = {
            'name': 'Fix',
            'task_type': self.task_type1.id,
            'show_my_tasks': True
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form_data = {}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data_in_task_type(self):
        form_data = {
            'name': 'Fix',
            'task_type': 9999,
            'show_my_tasks': True
        }
        form = TaskSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_checkbox_behavior(self):
        form_data = {
            'show_my_tasks': True
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['show_my_tasks'], True)

        form_data = {
            'show_my_tasks': False
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['show_my_tasks'], False)