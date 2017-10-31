from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import json

from .forms import TripForm, PointsOfInterestForm, PointsOfInterestModelForm
from .models import PointsOfInterest, Trip
from points.models import Point


def index(request):
    context = {}
    return render(request, 'trips/index.html', context)


def new(request):
    middle_points = []
    extra_point_number = 0

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

                for extra_point in range(int(extra_point_number)):
                    middle_points.append(points_form['extra_points_{ep}'.format(ep=extra_point)].value())

                middle_points.append(points_form['end_point'].value())
            except:
                # ToDo: Inform user about invalid input in case input is not empty
                # print(form['extra_points_{ep}'.format(ep=extra_point)].value())
                pass

            print('POINT FORM IS VALID')

            if trip_form.is_valid() and not ('add' in request.POST or 'clear' in request.POST):
                print('TRIP FORM IS VALID')

                trip = trip_form.save()
                points_model_form = PointsOfInterestModelForm()

                print('POINTS MODEL FORM IS VALID')

                new_points_set = points_model_form.save(commit=False)
                new_points_set.trip = trip
                new_points_set.points = json.dumps(middle_points)
                new_points_set.save()

    context = {
        'trip_form': trip_form,
        'points_form': points_form,
        'middle_points': middle_points,
        'extra_fields_number': range(int(extra_point_number))
    }

    return render(request, 'trips/new.html', context)




    #
    # print(trip)
    #
    #
    # if request.method != 'POST':
    #     points_form = PointsOfInterestForm(extra=0)
    #
    # else:
    #     points_model_form = PointsOfInterestModelForm(request.POST)
    #
    #     extra_point_number = request.POST.get('extra_points_count')
    #
    #     points_form = PointsOfInterestForm(request.POST, extra=extra_point_number)
    #
    #     if points_form.is_valid():
    #         middle_points.append(Point.objects.get(name=points_form['begin_point'].value()))
    #
    #         for extra_point in range(int(extra_point_number)):
    #             try:
    #                 middle_points.append(
    #                     Point.objects.get(name=points_form['extra_points_{ep}'.format(ep=extra_point)].value()))
    #             except:
    #                 # ToDo: Inform user about invalid input in case input is not empty
    #                 # print(form['extra_points_{ep}'.format(ep=extra_point)].value())
    #                 pass
    #
    #         middle_points.append(Point.objects.get(name=points_form['end_point'].value()))
    #         points_coordinates = []
    #
    #         for point in middle_points:
    #             points_coordinates.append([point.latitude, point.longitude])
    #
    #         points_model_form['points'] = json.dumps(points_coordinates)
    #         points_model_form['trip'] = trip
    #
    #         print(points_model_form)
    #
    #         if points_model_form.is_valid():
    #             points_model_form.save()


