
from django.forms import ModelForm, DateField, widgets
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields= ('dataTask','descrizione','spesa', 'completato' ,'dataCompletamento' )
        widgets = {
            'dataTask': widgets.DateInput(attrs={'type': 'date'},),
            'dataCompletamento': widgets.DateInput(attrs={'type': 'date'},),

        }
