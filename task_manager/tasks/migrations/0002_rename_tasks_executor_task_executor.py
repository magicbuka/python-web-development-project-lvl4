# Generated by Django 4.0.4 on 2022-07-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tasks_executor',
            new_name='executor',
        ),
    ]
