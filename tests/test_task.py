import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

import pytest
from rest_framework.test import APIClient

from task.models import Task

client = APIClient()


@pytest.mark.django_db
def test_get_task():
    response = client.get("/tasks/")
    print(response.data)


@pytest.mark.django_db
def test_post_task():
    task = {
        "description": "test desc"
    }
    response = client.post("/tasks/", task)
    print(response.data)


@pytest.mark.django_db
def test_update_task():
    task = {
        "description": "test desc",
        "status": "done"
    }
    response = client.put("/tasks/4/", task)
    print(response.data)


@pytest.mark.django_db
def test_delete_task():
    response = client.delete("/tasks/4/")
    print(response.data)

#### Сделать ошибки
