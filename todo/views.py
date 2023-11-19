from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    paginate_by = 10
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")
