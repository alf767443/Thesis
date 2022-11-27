from rest_framework import serializers
from RouteApplication.models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields=('RouteId', 'RouteDistanceEstimated', 'RouteConsumptionEstimated', 'RouteDistanceReal', 'RouteConsumptionReal', 'RouteStartPoint', 'RouteEndPoint')
