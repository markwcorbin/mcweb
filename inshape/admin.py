from django.contrib import admin
from .models import Routine, Exercise, Workout, WorkoutClimb

class RoutineAdmin(admin.ModelAdmin):
    fields = ['name', 'sequence']

class ExerciseAdmin(admin.ModelAdmin):
    fields = [ 'name', 'description', 'routine', 'sets', 'reps', 'warmup_weight',
              'weight', 'sequence']

class WorkoutAdmin(admin.ModelAdmin):
    fields = [ 'workout_date', 'routine', 'description']

class WorkoutClimbAdmin(admin.ModelAdmin):
    fields = ['workout', 'route_type', 'rating', 'notes']

admin.site.register(Routine, RoutineAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutClimb, WorkoutClimbAdmin)
