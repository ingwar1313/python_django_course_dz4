from django.urls import path

from . import views
from todo_list.views import (
    TaskDetailView,
    TaskDeleteView,
    TaskListView,
    TaskFormView,
    TaskViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
app_name = "api"
router.register(prefix="api/tasks", viewset=TaskViewSet, basename="tasks")

urlpatterns = router.urls + [
    path("", views.index, name="index"),
    path("tasks/<int:pk>", TaskDetailView.as_view()),
    path("tasks/view_all", TaskListView.as_view(), name="view_all_tasks"),
    path("task_delete/<int:pk>", TaskDeleteView.as_view()),
    path("task_edit/<int:pk>", TaskFormView.as_view()),
]
