# Generated by Django 2.1.1 on 2018-12-09 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0017_auto_20181111_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='workout_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 17, 26, 24, 278585)),
        ),
    ]
