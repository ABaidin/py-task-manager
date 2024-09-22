from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from accounts.forms import RegistrationForm
from task_manager_app.forms import TaskForm, TaskSearchForm
from task_manager_app.models import Task, TaskType, Position


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'task_manager/index.html'


# Task Views
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_manager/task_list.html"
    paginate_by = 10

    def get_queryset(self) -> QuerySet:
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET or None)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            task_type = form.cleaned_data.get("task_type")
            show_my_tasks = form.cleaned_data.get("show_my_tasks")

            if name:
                queryset = queryset.filter(name__icontains=name)

            if task_type:
                queryset = queryset.filter(task_type=task_type)

            if show_my_tasks:
                queryset = queryset.filter(assigned_to=self.request.user)

        return queryset

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        form = TaskSearchForm(self.request.GET or None)
        context["form"] = form

        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_manager/task_detail.html"
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_manager/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_manager/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_manager/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")


# Task Type Views
class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task_manager/task_type_list.html"
    context_object_name = "task_types"


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tasktype_list")


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tasktype_list")


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    template_name = "task_manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("tasktype_list")


# Position Views


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "task_manager/position_list.html"
    context_object_name = "positions"


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    template_name = "task_manager/position_form.html"
    fields = ["name"]
    success_url = reverse_lazy("position_list")


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    template_name = "task_manager/position_form.html"
    fields = ["name"]
    success_url = reverse_lazy("position_list")


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    template_name = "task_manager/position_confirm_delete.html"
    success_url = reverse_lazy("position_list")


# Employee Views


class EmployeeListView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = "task_manager/employee_list.html"
    context_object_name = "employees"


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "task_manager/employee_detail.html"
    context_object_name = "employee"


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    template_name = "task_manager/employee_form.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("employee_list")


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = "task_manager/employee_form.html"
    fields = ["username", "email", "first_name", "last_name", "position"]
    success_url = reverse_lazy("employee_list")


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = "task_manager/employee_confirm_delete.html"
    success_url = reverse_lazy("employee_list")
