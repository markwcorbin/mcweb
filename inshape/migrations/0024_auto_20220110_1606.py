# Generated by Django 2.1.1 on 2022-01-10 22:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0023_auto_20220110_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutStairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.TimeField()),
                ('floors', models.IntegerField(blank=True, null=True)),
                ('altitude_gain', models.IntegerField(blank=True, null=True)),
                ('avg_speed', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('time_in_zone', models.TimeField(blank=True, null=True)),
                ('avg_hr', models.IntegerField(blank=True, null=True)),
                ('max_hr', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 16, 6, 17, 500762)),
        ),
        migrations.AddField(
            model_name='workoutstairs',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inshape.Workout'),
        ),
    ]