from django.urls import path
from todo.views import (
    TaskListView,
    TaskCreateView,
    change_the_ready_state,
    TaskDeleteView,
    TaskUpdateView,

)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/change_state/",
        change_the_ready_state,
        name="change_state",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
]

app_name = "todo"
