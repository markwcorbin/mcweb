from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Routine
    path('routine/<int:routine_id>/', views.routine, name='routine'),
    # Exercise
    path('exercise/<int:exercise_id>/', views.exercise, name='exercise'),
    # Workout
    path('workout/<int:workout_type>', views.workout, name='workout'),
    path('workout_routine/<int:workout_id>/<int:routine_id>/', views.workout_routine, name='workout_routine' ),
    path('workout_strength/<int:exercise_id>/<int:routine_id>/<int:workout_id>', views.workout_strength, name='workout_strength' ),
    path('workout_biking/<int:workout_id>/', views.workout_biking, name='workout_biking'),
    path('invalid_entry/', views.invalid_entry, name='invalid_entry'),
    path('done/', views.done, name='done'),
]
