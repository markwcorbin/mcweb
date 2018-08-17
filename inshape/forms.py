from django import forms
from .models import Routine

def get_routines():
    routine_tuples = [(routine.pk, routine.name) for routine in Routine.objects.all()]
    return(routine_tuples)


class WorkoutForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['Routine'] = forms.ChoiceField(choices=get_routines() )

    workout_date = forms.DateTimeField()
    notes = forms.CharField(label='Notes:', max_length=100)


class WorkoutStrengthForm(forms.Form):
    name = forms.CharField(label='Name:')
    sets = forms.IntegerField(label='Sets:')
    reps = forms.IntegerField(label='Reps')
    weight = forms.IntegerField(label='Weight:')


