# Generated by Django 2.0 on 2018-02-10 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediumname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_number', models.IntegerField(default=0)),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='honoradar.Medium')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_number', models.IntegerField(default=0)),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='honoradar.Medium')),
            ],
        ),
    ]
