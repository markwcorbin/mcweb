# Generated by Django 2.0.3 on 2018-08-31 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0008_workout_workoutstrength'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutBiking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('distance', models.DecimalField(decimal_places=1, max_digits=4)),
                ('duration', models.TimeField()),
                ('avg_speed', models.DecimalField(decimal_places=1, max_digits=3)),
                ('time_in_zone', models.TimeField(blank=True, null=True)),
                ('avg_hr', models.IntegerField(blank=True, null=True)),
                ('max_hr', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inshape.Workout')),
            ],
        ),
    ]