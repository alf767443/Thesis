from rest_framework import serializers
from ActionsApplication.models import *

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actions
        fields=('ActionsId', 'ActionsAction', 'ActionsStatus', 'ActionsPriority', 'ActionsSource')

class QueueSerializer(serializers.ModelSerializer):
    actions = ActionsSerializer(read_only = True)

    class Meta:
        model=Queue
        fields=('QueueId','QueueStatus','ActionsId','actions')
        depth = 1