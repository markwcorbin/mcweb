# Generated by Django 2.1.1 on 2018-09-19 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0011_workout_workout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 19, 15, 14, 8, 855245)),
        ),
    ]