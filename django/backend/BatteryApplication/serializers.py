from rest_framework import serializers
from BatteryApplication.models import Physical, Status

class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Physical
        fields=('PhysicalId', 'PhysicalVoltage', 'PhysicalCurrent', 'PhysicalTemperature')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=('StatusId', 'StatusBattery')
