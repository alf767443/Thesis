from rest_framework import serializers
from BatteryApplication.models import *

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields=('__all__')

class CalculateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Calculate
        fields=('__all__')

class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model=Battery
        fields=('__all__')
        depth = 1
