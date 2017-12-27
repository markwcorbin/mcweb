from django.contrib import admin
from .models import Workout, Exercise

class WorkoutAdmin(admin.ModelAdmin):
    fields = ['name', 'sequence']

class ExerciseAdmin(admin.ModelAdmin):
    fields = [ 'name', 'description', 'workout', 'sets', 'reps', 'warmup_weight',
              'weight', 'sequence']

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)

