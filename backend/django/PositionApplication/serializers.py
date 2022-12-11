from rest_framework import serializers
from PositionApplication.models import *

class OdometrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Odometry
        fields=('__all__')

class FiducialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fiducial
        fields=('__all__')

class GyroscopeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gyroscope
        fields=('__all__')

class GlobalPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalPosition
        fields=('__all__')

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields=('__all__')
        depth = 1