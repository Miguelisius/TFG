# Generated by Django 5.0.6 on 2024-11-06 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_notas_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='pareja_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correcciones', to='myapp.alumno'),
        ),
    ]
