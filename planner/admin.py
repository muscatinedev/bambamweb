from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['dataTask','descrizione','spesa', 'completato' ,'dataCompletamento']

    def get_ordering(self, request):
        return ['-dataTask']  # sort case insensitive


admin.site.register(Task, TaskAdmin)
