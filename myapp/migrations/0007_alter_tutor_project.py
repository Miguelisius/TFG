# Generated by Django 5.0.6 on 2024-09-12 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tutor_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project'),
        ),
    ]
