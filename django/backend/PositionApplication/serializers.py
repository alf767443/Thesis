from rest_framework import serializers
from PositionApplication.models import Odometry, Fiducial, Gyroscope

class OdometrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Odometry
        fields=('OdometryId', 'OdometryLeft', 'OdometryRight')

class FiducialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fiducial
        fields=('FiducialId', 'FiducialMark')

class GyroscopeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gyroscope
        fields=('GyroscopeId', 'GyroscopeAngle')
