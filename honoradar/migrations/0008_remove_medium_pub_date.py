# Generated by Django 2.0 on 2018-02-11 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0007_auto_20180211_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medium',
            name='pub_date',
        ),
    ]