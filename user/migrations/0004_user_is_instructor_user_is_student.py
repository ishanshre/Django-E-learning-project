# Generated by Django 4.1.4 on 2023-01-01 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
