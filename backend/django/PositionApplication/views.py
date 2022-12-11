from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from pymongo import MongoClient

from PositionApplication.models import *
from PositionApplication.serializers import *

from django.core.files.storage import default_storage

# Odometry API
@csrf_exempt
def odometryApi(request,id=0):
    if request.method=='GET':
        odometry = Odometry.objects.all()
        odometry_serializer=OdometrySerializer(odometry,many=True)
        return JsonResponse(odometry_serializer.data,safe=False)
    
# Fiducial marks API
@csrf_exempt
def fiducialApi(request,id=0):
    if request.method=='GET':
        fiducial = Fiducial.objects.all()
        fiducial_serializer=FiducialSerializer(fiducial,many=True)
        return JsonResponse(fiducial_serializer.data,safe=False)

# Gyroscope API
@csrf_exempt
def gyroscopeApi(request,id=0):
    if request.method=='GET':
        gyroscope = Gyroscope.objects.all()
        gyroscope_serializer=GyroscopeSerializer(gyroscope,many=True)
        return JsonResponse(gyroscope_serializer.data,safe=False)
 
# Global position API
@csrf_exempt
def globalpositionApi(request,id=0):
    if request.method=='GET':
        globalposition = GlobalPosition.objects.all()
        globalposition_serializer=GlobalPositionSerializer(globalposition,many=True)
        return JsonResponse(globalposition_serializer.data,safe=False)

@csrf_exempt
def  positionApi(request,id=0):
    if request.method=='GET':
        position =  Position.objects.all()
        position_serializer= PositionSerializer( position,many=True)
        return JsonResponse(position_serializer.data,safe=False)
    elif request.method=='POST':
        position_data=JSONParser().parse(request)
        position_serializer= PositionSerializer(data= position_data)
        if position_serializer.is_valid():
            position_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        position_data=JSONParser().parse(request)
        position= Position.objects.get( PositionId= position_data[' PositionId'])
        position_serializer= PositionSerializer( position,data= position_data)
        if position_serializer.is_valid():
            position_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        position= Position.objects.get( PositionId=id)
        position.delete()
        return JsonResponse("Deleted Successfully",safe=False)
