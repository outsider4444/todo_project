import django
from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    time_create = models.DateTimeField(default=now)
