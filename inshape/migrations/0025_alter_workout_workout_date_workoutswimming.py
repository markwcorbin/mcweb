# Generated by Django 4.0.2 on 2023-10-31 17:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0024_auto_20220110_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 12, 33, 18, 507086)),
        ),
        migrations.CreateModel(
            name='WorkoutSwimming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.TimeField()),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=50, null=True)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inshape.workout')),
            ],
        ),
    ]
