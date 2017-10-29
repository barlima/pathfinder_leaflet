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


def new_trip(request):
    if request.method != 'POST':
        trip_form = TripForm()

    else:
        trip_form = TripForm(request.POST)

        if trip_form.is_valid():
            trip = trip_form.save()
            print(trip.id)
            return HttpResponseRedirect(reverse("trips:new_trip_data", args=[trip.id]))

    context = {
        'trip_form': trip_form,
    }

    return render(request, 'trips/new_trip.html', context)


def new_trip_data(request, trip_id):
    trip = Trip.objects.get(id=trip_id)

    if request.method != 'POST':
        points_form = PointsOfInterestModelForm()
    else:
        points_form = PointsOfInterestModelForm(request.POST)
        print(points_form)

        if points_form.is_valid():
            new_points_set = points_form.save(commit=False)
            new_points_set.trip = trip
            new_points_set.save()
            print(new_points_set)
            return HttpResponseRedirect(reverse('trips:new_trip'))

    context = {
        'points_form': points_form,
        'trip': trip
    }

    return render(request, 'trips/new_trip_data.html', context)


def new(request):
    middle_points = []

    if request.method != 'POST':
        trip_form = TripForm()
        points_form = PointsOfInterestForm(extra=0)
        print(points_form['extra_points_count'])
    else:
        extra_point_number = request.POST.get('extra_points_count')

        trip_form = TripForm(request.POST)
        points_form = PointsOfInterestForm(request.POST, extra=extra_point_number)

        if points_form.is_valid():
            middle_points.append(Point.objects.get(name=points_form['begin_point'].value()))

            for extra_point in range(int(extra_point_number)):
                try:
                    middle_points.append(
                        Point.objects.get(name=points_form['extra_points_{ep}'.format(ep=extra_point)].value()))
                except:
                    # ToDo: Inform user about invalid input in case input is not empty
                    # print(form['extra_points_{ep}'.format(ep=extra_point)].value())
                    pass

            middle_points.append(Point.objects.get(name=points_form['end_point'].value()))

            points_coordinates = []

            for point in middle_points:
                points_coordinates.append([point.latitude, point.longitude])

            print('POINT FORM IS VALID')

            if trip_form.is_valid():
                print('TRIP FORM IS VALID')

                trip = trip_form.save()
                points_model_form = PointsOfInterestModelForm()

                print('POINTS MODEL FORM IS VALID')

                new_points_set = points_model_form.save(commit=False)
                new_points_set.trip = trip
                new_points_set.points = json.dumps(points_coordinates)
                new_points_set.save()

    context = {
        'trip_form': trip_form,
        'points_form': points_form
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


