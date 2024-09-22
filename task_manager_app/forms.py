from django import forms
from task_manager_app.models import Task, TaskType


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name", "description", "deadline",
            "priority", "task_type", "assigned_to", "is_completed"
        ]
        widgets = {
            "assigned_to": forms.CheckboxSelectMultiple()
        }


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search by name..."
            }
        )
    )

    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        required=False,
        label="",
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="-- Filter by Task Type --"
    )

    show_my_tasks = forms.BooleanField(
        required=False,
        label="Show only my tasks",
        widget=forms.CheckboxInput()
    )
