from django import forms

from .models import Point


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
