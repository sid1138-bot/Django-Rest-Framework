# Generated by Django 4.2.2 on 2023-06-13 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_project_client_client_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='project',
        ),
    ]
