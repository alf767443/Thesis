from rest_framework import serializers
from BatteryApplication.models import Charge, Status

class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Charge
        fields=('ChargeId', 'ChargeVoltage')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=('StatusId', 'StatusBattery')
