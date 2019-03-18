# Generated by Django 2.1.7 on 2019-03-18 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interviewprep', '0002_course_lesson_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('answer', models.CharField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='users',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lessons',
        ),
        migrations.RemoveField(
            model_name='question',
            name='users',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='interviewprep.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='interviewprep.Lesson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviewprep.Question'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]