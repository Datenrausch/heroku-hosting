# Generated by Django 2.0 on 2018-02-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0005_datacollection_jobstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datacollection',
            name='jobstatus',
        ),
        migrations.AddField(
            model_name='medium',
            name='jobstatus',
            field=models.CharField(choices=[('fest', 'fest'), ('pauschal', 'pauschal'), ('frei', 'frei')], default='frei', max_length=10),
        ),
    ]
