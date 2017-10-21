from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from points.models import Point
from points.forms import PointForm, PointRadioForm


def index(request):
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
    points = Point.objects.all()
    middle_points = []

    if request.method != 'POST':
        form = PointForm(extra=0)
    else:
        extra_point_number = request.POST.get('extra_points_count')
        form = PointForm(request.POST, extra=extra_point_number)
        if form.is_valid():
            middle_points.append(Point.objects.get(name=form['begin_point'].value()))
            for extra_point in range(int(extra_point_number)):
                try:
                    middle_points.append(Point.objects.get(name=form['extra_points_{ep}'.format(ep=extra_point)].value()))
                except:
                    # ToDo: Inform user about invalid input in case input is not empty
                    print(form['extra_points_{ep}'.format(ep=extra_point)].value())

    context = {
        'form': form,
        'points': points,
        'middlePoints': middle_points,
    }

    return render(request, 'map/multi_point_path.html', context)
