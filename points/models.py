from django.db import models


class Point(models.Model):
    """Describes points of interest - coordinates, type and name"""
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=20)
    # type = models.ForeignKey(Type)

    def __str__(self):
        return "%s (%.2f, %.2f)" % (self.name, self.latitude, self.longitude)


# class Type(models.Model):
