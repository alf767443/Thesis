from django.db import models

# Create your models here.
class Route(models.Model):
    RouteId = models.AutoField(primary_key=True)
    RouteDistanceEstimated = models.FloatField()
    RouteConsumptionEstimated = models.FloatField()
    RouteDistanceReal = models.FloatField()
    RouteConsumptionReal = models.FloatField()
    RouteStartPoint = models.JSONField()
    RouteEndPoint = models.JSONField()