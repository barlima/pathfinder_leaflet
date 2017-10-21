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


class PointForm(forms.Form):
    CHOICES = [(point.name, point.name) for point in reversed(Point.objects.all())]

    radioField = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onchange': 'this.form.submit();'}),
        choices=CHOICES,
    )

    extra_sets_count = forms.ChoiceField(
        widget=forms.HiddenInput(),
    )

    # Add new set of radio buttons when '+' is clicked
    def __init__(self, *args, **kwargs):
        extra_sets = kwargs.pop('extra', 0)

        extra_sets = extra_sets if not type(extra_sets) != 'NoneType' else 1

        super().__init__(*args, **kwargs)
        self.fields['extra_sets_count'].initial = extra_sets

        for i in range(int(extra_sets)):
            self.fields['extra_sets_{i}'.format(i=i)] = forms.RadioSelect(attrs={'onchange': 'this.form.submit();'})


