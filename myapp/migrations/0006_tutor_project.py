# Generated by Django 5.0.6 on 2024-09-12 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_task_alumno_remove_task_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.project'),
        ),
    ]
