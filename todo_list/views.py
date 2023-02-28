from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import DetailView, CreateView, ListView, View
from django.views.generic.edit import DeleteView, UpdateView
from todo_list.forms import TaskForm
from todo_list.models import Task
from django.urls import reverse, reverse_lazy

from rest_framework import mixins, viewsets
from .serializers import TaskSerializer
from .filters import TaskFilterSet
from rest_framework.schemas.openapi import AutoSchema

"""в views.py создайте классы для управления вашей моделью из браузера 
(действия - просмотр\изменение\удаление записи)."""


def index(request):
    return HttpResponse("Hello, you're at todo_list index!!!")


class TaskDetailView(DetailView):
    """Представление для отображения одной задачи.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview
    """

    context_object_name = "task"
    queryset = Task.objects.filter()
    template_name = "task_detail.html"


class TaskListView(ListView):
    """Представление для отображения множества задач.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
    """

    context_object_name = "tasks_"
    queryset = Task.objects.filter()
    template_name = "task_list.html"


class TaskDeleteView(DeleteView):
    """Представление для удаления одной задачи"""

    model = Task
    template_name = "task_confirm_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("view_all_tasks")


class TaskFormView(UpdateView, DetailView):
    """Представление для редактирования одной задачи"""

    context_object_name = "task"
    queryset = Task.objects.filter()
    template_name = "task_edit.html"
    model = Task
    fields = ["name", "is_active"]
    success_url = reverse_lazy("view_all_tasks")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)


class TaskViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer
    filterset_class = TaskFilterSet

    schema = AutoSchema(tags=["Tasks"], component_name="Task", operation_id_base="Task")

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
