# Generated by Django 2.1.1 on 2021-11-23 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0019_auto_20190305_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutcardio',
            name='watts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 21, 37, 58, 439823)),
        ),
        migrations.AlterField(
            model_name='workoutcardio',
            name='avg_speed',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='workoutcardio',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]