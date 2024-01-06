from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def planner_view(request):
    tasks = Task.objects.all().order_by('dataTask')
    context = {'tasks': tasks, }

    return render(request, 'planner/planner.html', context)


def tasks_view(request):
    tasks = Task.objects.filter(completato=False).order_by('dataTask')
    context = {'tasks': tasks, }

    return render(request, 'planner/tasks.html', context)


def calendarPlanner_view(request):
    tasks = Task.objects.all().order_by('dataTask')
    days = []

    for t in tasks:
        dayTask = []
        days.append([t.dataTask, t.descrizione])

    context = {'days': days, }

    return render(request, 'planner/calendar_planner.html', context)



def tasks_create_view(request):
    submitted = False
    update=False
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/planner/tasks/')

    form = TaskForm()
    context = {'form': form, "update":update}

    return render(request, 'planner/update.html', context)


def task_update_view(request, pk):
    task = Task.objects.get(id=pk)
    update=True
    submitted = False
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            return redirect('/planner/tasks/')

    form = TaskForm(instance=task)
    context = {'form': form, "update":update}
    return render(request, 'planner/update.html', context)
