# Generated by Django 2.1.1 on 2021-11-23 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0021_auto_20211122_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 21, 57, 21, 783480)),
        ),
    ]
