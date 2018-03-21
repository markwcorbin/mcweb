from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Routine
    path('routine/<int:routine_id>/', views.routine, name='routine'),
    # Exercise
    path('exercise/<int:exercise_id>/', views.exercise, name='exercise'),
]

