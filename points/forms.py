from django import forms

from .models import Point


class PointRadioForm(forms.Form):
    CHOICES = (
        ('point_A', 'A'),
        ('point_B', 'B'),
        ('point_C', 'C'),
        ('point_D', 'D'),
        ('point_E', 'E'),
    )# This should takes values from Point model

    radioField = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
