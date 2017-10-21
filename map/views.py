from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from points.models import Point
from points.forms import PointForm, PointRadioForm


def index(request):
# def old_index(request):
    begin_point = Point()
    end_point = Point()
    points = Point.objects.all()

    if request.method != 'POST':
        form = PointRadioForm({'radioFieldBegin': 'A', 'radioFieldEnd': 'A'})
    else:
        form = PointRadioForm(request.POST)
        if form.is_valid():
            begin_point = Point.objects.get(name=form['radioFieldBegin'].value())
            end_point = Point.objects.get(name=form['radioFieldEnd'].value())

    context = {
        'beginPoint': begin_point,
        'endPoint': end_point,
        'points': points,
        'form': form,
    }
    return render(request, 'map/index.html', context)


def multi_point_path(request):
    return render(request, 'map/multi_point_path.html')
