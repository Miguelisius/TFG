# Generated by Django 5.0.6 on 2024-11-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_remove_notas_calificacion_descriptivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='calificacion_descriptivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
