from rest_framework import serializers
from MotorApplication.models import *

class VoltageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Voltage
        fields=('__all__')

class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Current
        fields=('__all__')
    
class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Power
        fields=('__all__')

class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Motor
        fields=('__all__')
        depth = 1