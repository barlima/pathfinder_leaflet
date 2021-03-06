from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import json

from .forms import TripForm, PointsOfInterestForm, PointsOfInterestModelForm
from .models import PointsOfInterest, Trip
from points.models import Point
from points.models import Point
from helpers.trips_helper import *


def index(request):
    context = {}
    return render(request, 'trips/index.html', context)


def show(request, points_set_id):
    points_set = PointsOfInterest.objects.get(id=points_set_id)

    distance, path = prepare_shortest_path(points_set.points, points_set.routes)
    points_shortest_path = clear_table(set_proper_order(points_set.points, path))
    # print(path)
    # print(distance)
    # print(points_shortest_path)

    points = []

    for point in points_shortest_path:
        p = Point()
        p.name = points_shortest_path.index(point)
        p.latitude = point[0]
        p.longitude = point[1]
        points.append(p)

    context = {
        'points': points
    }
    return render(request, 'trips/show.html', context)


def new(request):
    middle_points = []
    extra_point_number = 0
    links_and_values = ""

    if request.method != 'POST':
        trip_form = TripForm()
        points_form = PointsOfInterestForm(extra=0)
    else:
        extra_point_number = request.POST.get('extra_points_count')

        trip_form = TripForm(request.POST)
        points_form = PointsOfInterestForm(request.POST, extra=extra_point_number)

        if points_form.is_valid():

            try:
                middle_points.append(points_form['begin_point'].value())
                middle_points.append(points_form['end_point'].value())

                for extra_point in range(int(extra_point_number)):
                    middle_points.append(points_form['extra_points_{ep}'.format(ep=extra_point)].value())


            except:
                # ToDo: Inform user about invalid input in case input is not empty
                # print(form['extra_points_{ep}'.format(ep=extra_point)].value())
                pass

            print('--POINT FORM IS VALID--')

            if trip_form.is_valid() and not ('add' in request.POST or 'clear' in request.POST):
                print('--TRIP FORM IS VALID--')

                trip = trip_form.save()
                points_model_form = PointsOfInterestModelForm()

                print('--POINTS MODEL FORM IS VALID--')

                new_points_set = points_model_form.save(commit=False)
                new_points_set.trip = trip
                new_points_set.points = json.dumps(middle_points)
                new_points_set.routes = points_form['links_and_values'].value()
                new_points_set.save()

                return HttpResponseRedirect(reverse('trips:show', args=[new_points_set.id]))

    context = {
        'trip_form': trip_form,
        'points_form': points_form,
        'middle_points': middle_points,
        'all_points_range': range(len(middle_points)),
        'extra_fields_number': range(int(extra_point_number))
    }

    return render(request, 'trips/new.html', context)


