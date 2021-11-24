from django.db import models
from datetime import datetime

class Routine(models.Model):
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    routine = models.ManyToManyField(Routine)
    name = models.CharField(max_length=20)
    description = models.CharField(default=" ", max_length=200)
    sets = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    warmup_weight = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Workout(models.Model):
    workout_date = models.DateTimeField(default=datetime.now())
    workout_type = models.IntegerField(default=0)
    routine = models.IntegerField(default=0)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class WorkoutStrength(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    warmup_weight = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class WorkoutBiking(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    distance = models.DecimalField(decimal_places=1, max_digits=4)
    duration = models.TimeField()
    avg_speed = models.DecimalField(decimal_places=1, max_digits=3)
    time_in_zone = models.TimeField(blank=True, null=True)
    avg_hr = models.IntegerField(blank=True, null=True)
    max_hr = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)

class WorkoutClimb(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    route_type = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    notes = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.notes

class WorkoutRunning(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=True, null=True)
    distance = models.DecimalField(decimal_places=1, max_digits=4)
    duration = models.TimeField()
    avg_speed = models.DecimalField(decimal_places=1, max_digits=3)
    time_in_zone = models.TimeField(blank=True, null=True)
    avg_hr = models.IntegerField(blank=True, null=True)
    max_hr = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)

class WorkoutCardio(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=True, null=True)
    distance = models.DecimalField(decimal_places=1, max_digits=4, blank=True, null=True)
    duration = models.TimeField()
    avg_watts = models.IntegerField(blank=True, null=True)
    max_watts = models.IntegerField(blank=True, null=True)
    avg_speed = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    time_in_zone = models.TimeField(blank=True, null=True)
    avg_hr = models.IntegerField(blank=True, null=True)
    max_hr = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.description
        


