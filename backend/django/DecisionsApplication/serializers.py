from rest_framework import serializers
from DecisionsApplication.models import *

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administrator
        fields=('AdministratorId', 'AdministratorDecision', 'AdministratorPriority')

class RemoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Remote
        fields=('RemoteId', 'RemoteDecision', 'RemotePriority')

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Robot
        fields=('RobotId', 'RobotDecision', 'RobotPriority')
