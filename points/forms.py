from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Point


# Validators
# ToDo: Check how to make this vlidator working

def validate_point(value):
    if not Point.objects.filter(name=value):
        print("ValidationError")
        raise ValidationError(
            _('%(value)s is not a valid input'), params={'value': value}
        )


class PointRadioForm(forms.Form):
    CHOICES = [(point.name, point.name) for point in reversed(Point.objects.all())]

    radioFieldBegin = forms.ChoiceField(
                                    widget=forms.RadioSelect(attrs={'onchange': 'this.form.submit();'}),
                                    choices=CHOICES,
                                    )

    radioFieldEnd = forms.ChoiceField(
                                    widget=forms.RadioSelect(attrs={'onchange': 'this.form.submit();'}),
                                    choices=CHOICES,
                                    )


class PointForm(forms.Form):
    begin_point = forms.CharField(required=False, validators=[validate_point])

    extra_points_count = forms.CharField(widget=forms.HiddenInput())

    # Add new field of when '+' is clicked
    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        extra_fields = extra_fields if extra_fields else 1

        super().__init__(*args, **kwargs)
        self.fields['extra_points_count'].initial = extra_fields

        for i in range(int(extra_fields)):
            self.fields['extra_points_{i}'.format(i=i)] = forms.CharField(required=False, validators=[validate_point])


