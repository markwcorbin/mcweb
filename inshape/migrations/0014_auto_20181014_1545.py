# Generated by Django 2.1.1 on 2018-10-14 20:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0013_auto_20180925_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutClimbing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_type', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=10)),
                ('notes', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 14, 15, 45, 41, 969784)),
        ),
        migrations.AddField(
            model_name='workoutclimbing',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inshape.Workout'),
        ),
    ]