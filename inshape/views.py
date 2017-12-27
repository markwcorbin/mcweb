
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Workout, Exercise

def index(request):
    workout_list = Workout.objects.all()
    template = loader.get_template('inshape/index.html')
    context = {
        'workout_list': workout_list,
    }
    return HttpResponse(template.render(context, request))

def workout(request, workout_id):
    # Get exercises for this workout and display on page
    workout = Workout.objects.get(id=workout_id)
    exercises = Exercise.objects.filter(workout=workout_id)
    template = loader.get_template('inshape/workout.html')
    context = {
        'workout': workout,
        'exercises': exercises,
    }
    return HttpResponse(template.render(context, request))

def exercise(request, exercise_id):
    # Get an exercise and display it
    exercise = Exercise.objects.get(id=exercise_id)
    template = loader.get_template('inshape/exercise.html')
    context = {
        'exercise': exercise,
    }
    return HttpResponse(template.render(context, request))

