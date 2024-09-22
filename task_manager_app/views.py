from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from task_manager_app.forms import TaskForm, TaskSearchForm
from task_manager_app.models import Task


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
