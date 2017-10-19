from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from points.models import Point
from points.forms import PointRadioForm


def index(request):
    if request.method != 'POST':
        form = PointRadioForm()
    else:
        form = PointRadioForm(request.POST)
        if form.is_valid():
            pass

    context = {'points': Point.objects.all(), 'form': form}
    return render(request, 'map/index.html', context)
