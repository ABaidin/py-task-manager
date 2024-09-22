from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    TaskDeleteView,
)

app_name = "task_manager"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/detail/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
]
