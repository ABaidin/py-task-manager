from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    TaskDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    EmployeeListView,
    EmployeeCreateView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    IndexView,
)

app_name = "task_manager"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # Task URLs
    path("task/list/", TaskListView.as_view(), name="task_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/detail/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),

    # TaskType URLs
    path('tasktypes/', TaskTypeListView.as_view(), name='task_type_list'),
    path('tasktypes/create/', TaskTypeCreateView.as_view(), name='task_type_create'),
    path('tasktypes/<int:pk>/update/', TaskTypeUpdateView.as_view(), name='task_type_update'),
    path('tasktypes/<int:pk>/delete/', TaskTypeDeleteView.as_view(), name='task_type_delete'),

    # Position URLs
    path('positions/', PositionListView.as_view(), name='position_list'),
    path('positions/create/', PositionCreateView.as_view(), name='position_create'),
    path('positions/<int:pk>/update/', PositionUpdateView.as_view(), name='position_update'),
    path('positions/<int:pk>/delete/', PositionDeleteView.as_view(), name='position_delete'),

    # Employee URLs
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]
