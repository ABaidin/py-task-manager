from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)


class Employee(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class TaskType(models.Model):
    name = models.CharField(max_length=63, unique=True)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ManyToManyField(Employee, related_name="tasks")
    priority = models.CharField(
        choices=(
            ("LOW", "Low"),
            ("MEDIUM", "Medium"),
            ("HIGH", "High"),
            ("URGENT", "Urgent")
        ),
    )
