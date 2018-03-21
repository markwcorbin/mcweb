from django.db import models

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

    

