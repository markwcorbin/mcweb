# Generated by Django 2.0 on 2017-12-14 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inshape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inshape.Workout'),
        ),
    ]
