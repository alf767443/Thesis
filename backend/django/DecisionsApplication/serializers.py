from rest_framework import serializers
from DecisionsApplication.models import *

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administrator
        fields=('__all__')

class RemoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Remote
        fields=('__all__')

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Robot
        fields=('__all__')
