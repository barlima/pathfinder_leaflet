from django.db import models
from points.models import Point

import json


class Trip(models.Model):
    """Contains user data"""
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    # ToDo: Add field which contains all of the users points


class PointsOfInterest(models.Model):
    """Contains a list of points which are going to be visited by the user"""
    trip = models.ForeignKey(Trip)
    points = models.CharField(max_length=1000)

    def set_points(self, point):
        self.points = json.dumps(point)

    def get_points(self):
        return json.loads(self.points)
