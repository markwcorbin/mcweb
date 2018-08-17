
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Workout, Routine, Exercise
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

def workout_routine(request, routine_id):
    # Enter results of a workout for the selected routine
    routine = Routine.objects.get(id=routine_id)
    exercises = Exercise.objects.filter(routine=routine_id)
    template = loader.get_template('inshape/workout_routine.html')
    context = {
        'routine': routine,
        'exercises': exercises,
    }
    return HttpResponse(template.render(context, request))

def workout(request):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            workout_routine_url = '/inshape/workout_routine/' + str(form.cleaned_data.get('Routine'))
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

def workout_strength(request, exercise_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutStrengthForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/inshape/done/')
    # If a GET or any other method, create a blank form
    else:
        form = WorkoutStrengthForm()
        template = loader.get_template('inshape/workout_exercise.html')
        context = { 'form': form,
                    'exercise': exercise_id,
        }
        return HttpResponse(template.render(context, request))

def done(request):
    return render(request, 'inshape/done.html')

def invalid_entry(request):
    return render(request, 'inshape/invalid_entry.html')

