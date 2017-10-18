from django.shortcuts import render
from django.http import HttpResponse

from points.models import Point


def index(request):
    context = {'point': Point.objects.all()[0]}
    return render(request, 'map/index.html', context)
