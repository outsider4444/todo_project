# Generated by Django 4.0.6 on 2022-07-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_create',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
