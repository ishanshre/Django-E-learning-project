# Generated by Django 4.1.4 on 2023-01-22 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
    ]