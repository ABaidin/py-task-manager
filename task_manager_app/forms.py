from django import forms
from task_manager_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name", "description", "deadline",
            "priority", "task_type", "assigned_to",
        ]
        widgets = {
            "assigned_to": forms.CheckboxSelectMultiple()
        }