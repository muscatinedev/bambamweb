from django.db import models

class Task(models.Model):
    dataTask = models.DateField(null=True, blank=True)
    descrizione = models.CharField(max_length=290)
    spesa = models.FloatField(null=True, blank=True)
    dataCompletamento = models.DateField(null=True, blank=True)
    completato = models.BooleanField(default=False)


