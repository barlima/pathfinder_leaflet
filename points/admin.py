from django.contrib import admin
from points.models import Point
from trips.models import PointsOfInterest, Trip

admin.site.register(Point)
admin.site.register(Trip)
admin.site.register(PointsOfInterest)
