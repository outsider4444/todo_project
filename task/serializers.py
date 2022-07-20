import django.utils.timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    time_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M',required=False)

    class Meta:
        model = Task
        fields = ('id', 'description', 'status', 'time_create')
