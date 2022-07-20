from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskTest(APITestCase):

    def setUp(self):
        Task.objects.create(id=1, description="Задание для проверки", status="todo")
        Task.objects.create(id=2,description="Задание для проверки 2", status="todo", )

    def test_step1_get_all_tasks(self):
        tasks_count = len(Task.objects.all())
        response = self.client.get("/tasks/")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), tasks_count)
        self.assertEqual(len(response.data), 2)

    def test_step2_tasks_update(self):
        response = self.client.put(f"/tasks/1/", {"description": "Задание для проверки изменений", "status": "done"})
        self.assertEqual(response.data, {"id": 1, "description": "Задание для проверки изменений", "status": "done", "time_create" :response.data['time_create']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_step3_tasks_delete_db(self):
        task_to_delete = Task.objects.get(id=1)
        task_to_delete.delete()
        tasks_count = len(Task.objects.all())
        print(tasks_count)
        self.assertEqual(tasks_count, 1)

    def test_step4_tasks_create(self):
        new_task = {'description':"Задание для проверки функции создания", 'status':'todo'}
        response = self.client.post(f"/tasks/", new_task)
        tasks_count = len(Task.objects.all())
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tasks_count, 3)

    def test_step5_tasks_detail(self):
        response = self.client.get("/tasks/2/")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_step6_tasks_detail_error(self):
        response = self.client.get("/tasks/3/")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)