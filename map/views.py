from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from points.models import Point
from points.forms import PointRadioForm


def index(request):
    pathPoints = ()
    beginPoint = Point()
    endPoint = Point()
    points = Point.objects.all()

    if request.method != 'POST':
        form = PointRadioForm({'radioFieldBegin': 'A', 'radioFieldEnd': 'A'})
    else:
        form = PointRadioForm(request.POST)
        if form.is_valid():
            beginPoint = Point.objects.get(name=form['radioFieldBegin'].value())
            endPoint = Point.objects.get(name=form['radioFieldEnd'].value())

    context = {
        'beginPoint': beginPoint,
        'endPoint': endPoint,
        'points': points,
        'form': form
    }
    return render(request, 'map/index.html', context)
