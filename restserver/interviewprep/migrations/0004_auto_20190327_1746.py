# Generated by Django 2.1.7 on 2019-03-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewprep', '0003_auto_20190327_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='accuracy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='totalscore',
            field=models.IntegerField(default=0),
        ),
    ]
