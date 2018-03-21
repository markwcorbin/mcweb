from django.contrib import admin
from .models import Routine, Exercise

class RoutineAdmin(admin.ModelAdmin):
    fields = ['name', 'sequence']

class ExerciseAdmin(admin.ModelAdmin):
    fields = [ 'name', 'description', 'routine', 'sets', 'reps', 'warmup_weight',
              'weight', 'sequence']

admin.site.register(Routine, RoutineAdmin)
admin.site.register(Exercise, ExerciseAdmin)

