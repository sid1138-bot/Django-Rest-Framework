# Generated by Django 4.2.2 on 2023-06-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
    ]
