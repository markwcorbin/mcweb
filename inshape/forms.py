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
    notes = forms.CharField(label='Notes:', max_length=100)


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
    distance = forms.DecimalField(label='Distance', max_digits=4)
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Duration')
    avg_speed = forms.DecimalField(label='Avg Speed', max_digits=3)
    time_in_zone = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='In Heart Rate Zone')
    avg_hr = forms.IntegerField(label='Avg Heart Rate')
    max_hr = forms.IntegerField(label='Max Heart Rate')
    notes = forms.CharField(label='Notes') 