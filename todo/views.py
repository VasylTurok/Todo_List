from django.shortcuts import render, redirect
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


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("taxi:index")


def change_the_ready_state(request, pk):
    task = Task.objects.get(id=pk)
    task.done = not task.done
    print(task.done)
    task.save()
    next_url = request.GET.get('next', '/')
    return redirect(next_url)
