# Generated by Django 3.0.6 on 2020-06-24 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuserapp', '0002_myuser_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='age',
        ),
    ]
