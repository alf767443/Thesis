from rest_framework import serializers
from ActionsApplication.models import *

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actions
        fields=('ActionsId', 'ActionsAction', 'ActionsStatus', 'ActionsPriority', 'ActionsSource')
