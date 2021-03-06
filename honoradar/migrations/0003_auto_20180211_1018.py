# Generated by Django 2.0 on 2018-02-11 10:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0002_medium_rating_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='salary_number',
            new_name='rating_number',
        ),
        migrations.AddField(
            model_name='medium',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 10, 18, 49, 879242, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
