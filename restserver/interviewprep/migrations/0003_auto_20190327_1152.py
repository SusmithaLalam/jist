# Generated by Django 2.1.7 on 2019-03-27 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewprep', '0002_auto_20190327_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='lesson_count',
            new_name='lessoncount',
        ),
    ]
