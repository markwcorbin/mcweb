from django import forms
from .models import Routine

def get_routines():
    routine_tuples = [(routine.pk, routine.name) for routine in Routine.objects.all()]
    return(routine_tuples)


class WorkoutForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['Routine'] = forms.ChoiceField(choices=get_routines() )

    workout_type = forms.IntegerField(widget=forms.HiddenInput)
    workout_date = forms.DateTimeField()
    description = forms.CharField(label='Description:', max_length=100)


class WorkoutStrengthForm(forms.Form):
    workout = forms.IntegerField(widget=forms.HiddenInput)
    routine = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(label='Name:')
    sets = forms.IntegerField(label='Sets:')
    reps = forms.IntegerField(label='Reps')
    weight = forms.IntegerField(label='Weight:')

class WorkoutBikingForm(forms.Form):
    workout = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(label='Name')
    distance = forms.DecimalField(label='Distance (miles 00.0)', max_digits=4)
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Duration (hh:mm)')
    avg_speed = forms.DecimalField(label='Avg Speed (00.0)', max_digits=3)
    time_in_zone = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='In Heart Rate Zone (hh:mm)', required=False)
    avg_hr = forms.IntegerField(label='Avg Heart Rate', required=False)
    max_hr = forms.IntegerField(label='Max Heart Rate', required=False)
    notes = forms.CharField(label='Notes', required=False )

class WorkoutClimbForm(forms.Form):
    workout = forms.IntegerField(widget=forms.HiddenInput)
    route_type = forms.CharField(label='Route Type:')
    rating = forms.CharField(label='Rating:')
    notes = forms.CharField(label='Notes:', required=False)

class WorkoutRunningForm(forms.Form):
    workout = forms.IntegerField(widget=forms.HiddenInput)
    description = forms.CharField(label='Description')
    distance = forms.DecimalField(label='Distance (miles 00.0)', max_digits=4)
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Duration (hh:mm)')
    avg_speed = forms.DecimalField(label='Avg Speed (00.0)', max_digits=3)
    time_in_zone = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='In Heart Rate Zone (hh:mm)', required=False)
    avg_hr = forms.IntegerField(label='Avg Heart Rate', required=False)
    max_hr = forms.IntegerField(label='Max Heart Rate', required=False)
    notes = forms.CharField(label='Notes', required=False )

class WorkoutCardioForm(forms.Form):
    workout = forms.IntegerField(widget=forms.HiddenInput)
    description = forms.CharField(label='Description')
    distance = forms.DecimalField(label='Distance (miles 00.0)', max_digits=4, required=False)
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Duration (hh:mm)')
    avg_watts = forms.IntegerField(label='Avg Watts', required=False)
    max_watts = forms.IntegerField(label='Max Watts', required=False)
    avg_speed = forms.DecimalField(label='Avg Speed (00.0)', max_digits=3, required=False)
    time_in_zone = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='In Heart Rate Zone (hh:mm)', required=False)
    avg_hr = forms.IntegerField(label='Avg Heart Rate', required=False)
    max_hr = forms.IntegerField(label='Max Heart Rate', required=False)
    notes = forms.CharField(label='Notes', required=False )

class WorkoutSearchForm(forms.Form):
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
