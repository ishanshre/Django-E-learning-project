# Generated by Django 4.1.4 on 2023-01-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_courses_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='preview',
            field=models.ImageField(default='default/default_prevew.jpg', upload_to='courses/preview'),
        ),
    ]
