from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import PointsOfInterest, Trip


class TripForm(forms.ModelForm):
    """To contain main infos about the trip"""
    class Meta:
        model = Trip
        fields = ['name', 'start_date', 'end_date']
        labels = {'name': 'Name'}
        # name = forms.CharField(max_length=20)
        # start_date = forms.DateField()
        # end_date = forms.DateField()


class PointsOfInterestModelForm(forms.ModelForm):
    """To contain all of the points of interest"""
    class Meta:
        model = PointsOfInterest
        fields = []
        labels = {}


class PointsOfInterestForm(forms.Form):

    extra_points_count = forms.CharField(widget=forms.HiddenInput())

    # Add a new field of when '+' is clicked
    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        extra_fields = extra_fields if extra_fields else 0

        super().__init__(*args, **kwargs)
        self.fields['extra_points_count'].initial = extra_fields

        self.fields['begin_point'] = forms.CharField()
        self.fields['end_point'] = forms.CharField()

        for i in range(int(extra_fields)):
            # Not sure if this should be here
            self.fields['extra_points_{i}'.format(i=i)] = forms.CharField(required=False)

