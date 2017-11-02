from django.db import models
from points.models import Point

import json


class Trip(models.Model):
    """Contains user data"""
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%s (%s - %s)" % (self.name, self.start_date, self.end_date)


class PointsOfInterest(models.Model):
    """Contains a list of points which are going to be visited by the user"""
    trip = models.ForeignKey(Trip)
    points = models.TextField(default='')
    routes = models.TextField(default='')

    def set_points(self, point):
        self.points = json.dumps(point)

    def get_points(self):
        return json.loads(self.points)

    def __str__(self):
        return 'Points of trip %s' % self.trip.name
