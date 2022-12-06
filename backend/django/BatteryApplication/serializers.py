from rest_framework import serializers
from BatteryApplication.models import *

class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Physical
        fields=('PhysicalId', 'PhysicalVoltage', 'PhysicalCurrent', 'PhysicalTemperature')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=('StatusId', 'StatusBattery', 'StatusPercent')



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
        depth = 2
