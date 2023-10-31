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
    path('workout_climbing/<int:workout_id>/', views.workout_climbing, name='workout_climbing'),
    path('workout_climb/<int:workout_id>/', views.workout_climb, name='workout_climb'),
    path('workout_running/<int:workout_id>/', views.workout_running, name='workout_running'),
    path('workout_cardio/<int:workout_id>/', views.workout_cardio, name='workout_cardio'),
    path('workout_stairs/<int:workout_id>/', views.workout_stairs, name='workout_stairs'),
    path('workout_swimming/<int:workout_id>/', views.workout_swimming, name='workout_swimming'),
    path('workout_content/<int:workout_id>/', views.workout_content, name='workout_content'),
    path('workout_search/', views.workout_search, name='workout_search'),
    path('invalid_entry/', views.invalid_entry, name='invalid_entry'),
    path('done/', views.done, name='done'),
]
