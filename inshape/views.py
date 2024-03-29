
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import *
from .models import Workout, Routine, Exercise, WorkoutStrength, WorkoutBiking, WorkoutClimb, WorkoutRunning, WorkoutCardio, WorkoutStairs, WorkoutSwimming
from .forms import WorkoutForm
from .forms import WorkoutStrengthForm
from .forms import WorkoutBikingForm
from .forms import WorkoutClimbForm
from .forms import WorkoutRunningForm
from .forms import WorkoutSearchForm
from .forms import WorkoutCardioForm
from .forms import WorkoutStairsForm
from .forms import WorkoutSwimmingForm

def index(request):
    routine_list = Routine.objects.all()
    workout_list = Workout.objects.all().order_by('-workout_date')[:10]
    template = loader.get_template('inshape/index.html')
    context = {
        'routine_list': routine_list,
        'workout_list': workout_list,
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

def workout(request, workout_type):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Save Workout to the DB
            w = Workout()
            w.workout_date = form.cleaned_data.get('workout_date')
            w.workout_type = workout_type
            w.routine = form.cleaned_data.get('Routine')
            w.description = form.cleaned_data.get('description')
            w.save()
            # ToDo: add workout_id to workout_routine_url
            # Direct URL to workout type
            if (workout_type == 1):
                workout_routine_url = '/inshape/workout_routine/' \
                    + str(w.id) + '/' + str(form.cleaned_data.get('Routine'))
                return HttpResponseRedirect(workout_routine_url)
            elif (workout_type == 2):
                workout_biking_url = '/inshape/workout_biking/' \
                    + str(w.id) + '/'
                return HttpResponseRedirect(workout_biking_url)
            elif (workout_type == 3):
                workout_climbing_url = '/inshape/workout_climbing/' \
                    + str(w.id) + '/'
                return HttpResponseRedirect(workout_climbing_url)
            elif (workout_type == 4):
                workout_running_url = '/inshape/workout_running/' \
                    + str(w.id) + '/'
                return HttpResponseRedirect(workout_running_url)
            elif (workout_type == 5):
                workout_cardio_url = '/inshape/workout_cardio/' \
                    + str(w.id) + '/'
                return HttpResponseRedirect(workout_cardio_url)
            elif (workout_type == 6):
                workout_stairs_url = '/inshape/workout_stairs/' \
                    + str(w.id) + '/'
                return HttpResponseRedirect(workout_stairs_url)
            elif (workout_type == 7):
                workout_swimming_url = '/inshape/workout_swimming/' \
                    + str(w.id) + '/'
                return HttpResponseRedirect(workout_swimming_url)
            else:
                # Invalid workout type
                # ToDo: better error reporting
                return HttpResponseRedirect('/inshape/invalid_entry')
        else:
            # Something invalid in the form
            # ToDo: determine what field is in error
            return HttpResponseRedirect('/inshape/invalid_entry/')
    # If a GET or any other method, create a blank form/
    else:
        form = WorkoutForm(initial={'workout_type': workout_type})
        template = loader.get_template('inshape/workout.html')
        context = { 'form': form,
                    'workout_type': workout_type,
        }
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
        exercise = Exercise.objects.get(id=exercise_id)
        form = WorkoutStrengthForm(initial={'routine': routine_id, 'workout': workout_id})
        template = loader.get_template('inshape/workout_exercise.html')
        context = { 'form': form,
                    'exercise': exercise,
        }
        return HttpResponse(template.render(context, request))

def workout_biking(request, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutBikingForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            wb = WorkoutBiking()
            wb.workout = workout
            wb.name = form.cleaned_data.get('name')
            wb.distance = form.cleaned_data.get('distance')
            wb.duration = form.cleaned_data.get('duration')
            wb.avg_speed = form.cleaned_data.get('avg_speed')
            wb.time_in_zone = form.cleaned_data.get('time_in_zone')
            wb.avg_hr = form.cleaned_data.get('avg_hr')
            wb.max_hr = form.cleaned_data.get('max_hr')
            wb.avg_watts = form.cleaned_data.get('avg_watts')
            wb.max_watts = form.cleaned_data.get('max_watts')
            wb.notes = form.cleaned_data.get('notes')
            wb.save()
            # Go back to home page
            home_url = ('/inshape/')
            return HttpResponseRedirect(home_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutBikingForm(initial={'workout': workout_id})
        template = loader.get_template('inshape/workout_biking.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))

def workout_climbing(request, workout_id):
    # Enter results of a climbing session
    workout = Workout.objects.get(id=workout_id)
    climbs = WorkoutClimb.objects.filter(workout=workout_id)
    template = loader.get_template('inshape/workout_climbing.html')
    context = {
        'workout': workout,
        'climbs': climbs,
    }
    templateTest = template.render(context, request)
    print(templateTest)
    return HttpResponse(template.render(context, request))

def workout_climb(request, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutClimbForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            wc = WorkoutClimb()
            wc.workout = workout
            wc.route_type = form.cleaned_data.get('route_type')
            wc.rating = form.cleaned_data.get('rating')
            wc.notes = form.cleaned_data.get('notes')
            wc.save()
            # Go back to workout climbing page
            back_url = '/inshape/workout_climbing/' + str(workout.id)
            return HttpResponseRedirect(back_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutClimbForm(initial={'workout': workout_id})
        template = loader.get_template('inshape/workout_climb.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))

def workout_running(request, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutRunningForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            wb = WorkoutRunning()
            wb.workout = workout
            wb.description = form.cleaned_data.get('description')
            wb.distance = form.cleaned_data.get('distance')
            wb.duration = form.cleaned_data.get('duration')
            wb.avg_speed = form.cleaned_data.get('avg_speed')
            wb.time_in_zone = form.cleaned_data.get('time_in_zone')
            wb.avg_hr = form.cleaned_data.get('avg_hr')
            wb.max_hr = form.cleaned_data.get('max_hr')
            wb.notes = form.cleaned_data.get('notes')
            wb.save()
            # Go back to home page
            home_url = ('/inshape/')
            return HttpResponseRedirect(home_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutRunningForm(initial={'workout': workout_id})
        template = loader.get_template('inshape/workout_running.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))


def workout_cardio(request, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutCardioForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            wb = WorkoutCardio()
            wb.workout = workout
            wb.description = form.cleaned_data.get('description')
            wb.distance = form.cleaned_data.get('distance')
            wb.duration = form.cleaned_data.get('duration')
            wb.avg_watts = form.cleaned_data.get('avg_watts')
            wb.max_watts = form.cleaned_data.get('max_watts')
            wb.avg_speed = form.cleaned_data.get('avg_speed')
            wb.time_in_zone = form.cleaned_data.get('time_in_zone')
            wb.avg_hr = form.cleaned_data.get('avg_hr')
            wb.max_hr = form.cleaned_data.get('max_hr')
            wb.notes = form.cleaned_data.get('notes')
            wb.save()
            # Go back to home page
            home_url = ('/inshape/')
            return HttpResponseRedirect(home_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutCardioForm(initial={'workout': workout_id})
        template = loader.get_template('inshape/workout_cardio.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))

def workout_stairs(request, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutStairsForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            wb = WorkoutStairs()
            wb.workout = workout
            wb.description = form.cleaned_data.get('description')
            wb.floors = form.cleaned_data.get('floors')
            wb.altitude_gain = form.cleaned_data.get('altitude_gain')
            wb.duration = form.cleaned_data.get('duration')
            wb.avg_speed = form.cleaned_data.get('avg_speed')
            wb.time_in_zone = form.cleaned_data.get('time_in_zone')
            wb.avg_hr = form.cleaned_data.get('avg_hr')
            wb.max_hr = form.cleaned_data.get('max_hr')
            wb.notes = form.cleaned_data.get('notes')
            wb.save()
            # Go back to home page
            home_url = ('/inshape/')
            return HttpResponseRedirect(home_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutStairsForm(initial={'workout': workout_id})
        template = loader.get_template('inshape/workout_stairs.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))


def workout_swimming(request, workout_id):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutSwimmingForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            workout = Workout.objects.get(id=workout_id)
            wb = WorkoutSwimming()
            wb.workout = workout
            wb.description = form.cleaned_data.get('description')
            wb.duration = form.cleaned_data.get('duration')
            wb.distance = form.cleaned_data.get('distance')
            wb.notes = form.cleaned_data.get('notes')
            wb.save()
            # Go back to home page
            home_url = ('/inshape/')
            return HttpResponseRedirect(home_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')
        
    # If a GET or any other method, create a blank form
    else:
        form = WorkoutSwimmingForm(initial={'workout': workout_id})
        template = loader.get_template('inshape/workout_swimming.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))

def workout_content(request, workout_id):
    # Display content of the selected workout.  The template sorts out
    # what data fields to display based on the workout type
    workout_instance = Workout.objects.get(id=workout_id)
    workout_detail = get_workout_content_detail(workout_instance)
    if ( workout_detail ):
        template = loader.get_template('inshape/workout_content.html')
        context = {
            'workout_id': workout_id,
            'workout': workout_instance,
            'workout_detail': workout_detail,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/inshape/invalid_entry/')    

def workout_search(request):
    # If request is a POST, then process submitted data
    if request.method == 'POST':
        form = WorkoutSearchForm(request.POST)
        if form.is_valid():
            # Need to extract hidden Routine ID, Exercise ID and other fields,
            # then save them to DB
            print(form.cleaned_data)
            # Prepare query date parameters for start and end
            start_year = (form.cleaned_data.get('start_date')).year
            start_month = (form.cleaned_data.get('start_date')).month
            start_day = (form.cleaned_data.get('start_date')).day
            query_start_date = (str(start_year) + '-' + str(start_month) + '-' 
                                + str(start_day))
            end_year = (form.cleaned_data.get('end_date')).year
            end_month = (form.cleaned_data.get('end_date')).month
            end_day = (form.cleaned_data.get('end_date')).day
            query_end_date = (str(end_year) + '-' + str(end_month) + '-' 
                                + str(end_day))

            # Get workouts for specified date range
            w = (Workout.objects.filter(workout_date__gte=query_start_date)
                                        .filter(workout_date__lte=query_end_date).order_by('workout_date'))           
            template = loader.get_template('inshape/search_result_list.html')
            context = {
                'workout_list': w,
            }
            return HttpResponse(template.render(context, request))
            
            #back_url = '/inshape/'
            #return HttpResponseRedirect(back_url)
        else:
            return HttpResponseRedirect('/inshape/invalid_entry/')

    # If a GET or any other method, create a blank form
    else:
        form = WorkoutSearchForm()
        template = loader.get_template('inshape/workout_search.html')
        context = { 'form': form }
        return HttpResponse(template.render(context, request))

def get_workout_content_detail(workout_instance):
    # Get object containing details for the workout based on the type of workout
    if ( workout_instance.workout_type == 1):    # Type 1 is a strength workout
        workout_detail = WorkoutStrength.objects.filter(workout__id=workout_instance.id)
    if ( workout_instance.workout_type == 2):    # Type 2 is a biking workout
        workout_detail = WorkoutBiking.objects.filter(workout__id=workout_instance.id)
    if ( workout_instance.workout_type == 3):    # Type 3 is a climbing workout
        workout_detail = WorkoutClimb.objects.filter(workout_id=workout_instance.id)
    if ( workout_instance.workout_type == 4):    # Type 4 is a running workout
        workout_detail = WorkoutRunning.objects.filter(workout__id=workout_instance.id)
    if ( workout_instance.workout_type == 5):    # Type 5 is a cardio workout
        workout_detail = WorkoutCardio.objects.filter(workout__id=workout_instance.id)
    if ( workout_instance.workout_type == 6):    # Type 6 is a stairs workout
        workout_detail = WorkoutStairs.objects.filter(workout__id=workout_instance.id)
    if ( workout_instance.workout_type == 7):    # Type 7 is a swimming workout
        workout_detail = WorkoutSwimming.objects.filter(workout__id=workout_instance.id)

    return(workout_detail)

def done(request):
    return render(request, 'inshape/done.html')

def invalid_entry(request):
    return render(request, 'inshape/invalid_entry.html')

