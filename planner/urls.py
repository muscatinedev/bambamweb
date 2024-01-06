from django.contrib import admin
from django.urls import path

from planner.views import planner_view, task_update_view, calendarPlanner_view, tasks_view, tasks_create_view

urlpatterns = [
    path('', planner_view, name= "home-planner"),
    path('calendar/', calendarPlanner_view, name= "home-planner-calendar"),
    path('tasks/', tasks_view, name= "tasks-view"),
    path('tasks/create', tasks_create_view, name= "tasks-create"),

    path('task/<int:pk>/edit', task_update_view, name= "task-update"),

]