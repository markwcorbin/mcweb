
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import *
from .models import Workout, Routine, Exercise, WorkoutStrength
from .forms import WorkoutForm
from .forms import WorkoutStrengthForm

def index(request):
    routine_list = Routine.objects.all()
    template = loader.get_template('inshape/index.html')
    context = {
        'routine_list': routine_list,
    }
    return HttpResponse(template.render(context, request))

def routine(request, routine_id):
    # Get exercises for this routine and display on page
    routine = Routine.objects.get(id=routine_id)
    exercises = Exercise.objects.filter(routine=routine_id)
    template = loader.get_template('inshape/routine.html')
    context = {
        'routine': routine,
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

def workout_routine(request, workout_id, routine_id):
    # Enter results of a workout for the selected routine
    workout = Workout.objects.get(id=workout_id)
    routine = Routine.objects.get(id=routine_id)
    exercises = Exercise.objects.filter(routine=routine_id)
    template = loader.get_template('inshape/workout_routine.html')
    context = {
        'workout': workout,
        'routine': routine,
        'exercises': exercises,
    }
    templateTest = template.render(context, request)
    print(templateTest)
    return HttpResponse(template.render(context, request))

def workout(request):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Save Workout to the DB
            w = Workout()
            w.workout_date = form.cleaned_data.get('workout_date')
            w.routine = form.cleaned_data.get('Routine')
            w.notes = form.cleaned_data.get('notes')
            w.save()
            # ToDo: add workout_id to workout_routine_url
            workout_routine_url = '/inshape/workout_routine/' \
                + str(w.id) + '/' + str(form.cleaned_data.get('Routine'))
            return HttpResponseRedirect(workout_routine_url)
        else:
            # Something invalid in the form
            # ToDo: determine what field is in error
            return HttpResponseRedirect('/inshape/invalid_entry/')
    # If a GET or any other method, create a blank form/
    else:
        form = WorkoutForm()
        template = loader.get_template('inshape/workout.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))
#    return render(request, 'inshape/workout_name.html', {'form': form})

def workout_strength(request, exercise_id, routine_id, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutStrengthForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            ws = WorkoutStrength()
            ws.workout = workout
            ws.name = form.cleaned_data.get('name')
            ws.sets = form.cleaned_data.get('sets')
            ws.reps = form.cleaned_data.get('reps')
            ws.weight = form.cleaned_data.get('weight')
            ws.save()
            # Go back to Workout Routine page
            workout_routine_url = ('/inshape/workout_routine/' 
                + str(form.cleaned_data.get('workout')) + '/' 
                + str(form.cleaned_data.get('routine'))
            )
            return HttpResponseRedirect(workout_routine_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutStrengthForm(initial={'routine': routine_id, 'workout': workout_id})
        template = loader.get_template('inshape/workout_exercise.html')
        context = { 'form': form,
                    'exercise': exercise_id,
        }
        return HttpResponse(template.render(context, request))

def done(request):
    return render(request, 'inshape/done.html')

def invalid_entry(request):
    return render(request, 'inshape/invalid_entry.html')

