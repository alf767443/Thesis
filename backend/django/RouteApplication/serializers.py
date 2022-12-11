from rest_framework import serializers
from RouteApplication.models import *


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('__all__')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields=('__all__')
        depth = 1
