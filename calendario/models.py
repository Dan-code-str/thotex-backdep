from django.db import models

# Create your models here.

class Evento(models.Model):
    allDay = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.titulo