from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from task_manager_app.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    paginate_by = 10

    def get_queryset(self):
        show_my_tasks = self.request.GET.get("show_my_tasks")

        if show_my_tasks:
            return Task.objects.filter(assigned_to=self.request.user)
        else:
            return Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_my_tasks"] = self.request.GET.get("show_my_tasks")
        return context
