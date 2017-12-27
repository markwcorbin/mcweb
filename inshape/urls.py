from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Workout
    path('workout/<int:workout_id>/', views.workout, name='workout'),
    # Exercise
    path('exercise/<int:exercise_id>/', views.exercise, name='exercise'),
]

