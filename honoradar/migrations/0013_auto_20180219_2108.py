# Generated by Django 2.0 on 2018-02-19 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0012_auto_20180219_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datacollection',
            old_name='SalaryPerMonthEmp',
            new_name='SalaryPerMonthEmpMix',
        ),
    ]