from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PositionApplication.models import Odometry, Fiducial, Gyroscope, GlobalPosition
from PositionApplication.serializers import OdometrySerializer, FiducialSerializer, GyroscopeSerializer, GlobalPositionSerializer

from django.core.files.storage import default_storage

# Odometry API
@csrf_exempt
def odometryApi(request,id=0):
    if request.method=='GET':
        odometry = Odometry.objects.all()
        odometry_serializer=OdometrySerializer(odometry,many=True)
        return JsonResponse(odometry_serializer.data,safe=False)
    elif request.method=='POST':
        odometry_data=JSONParser().parse(request)
        odometry_serializer=OdometrySerializer(data=odometry_data)
        if odometry_serializer.is_valid():
            odometry_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        odometry_data=JSONParser().parse(request)
        odometry=Odometry.objects.get(OdometryId=odometry_data['OdometryId'])
        odometry_serializer=OdometrySerializer(odometry,data=odometry_data)
        if odometry_serializer.is_valid():
            odometry_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        odometry=Odometry.objects.get(OdometryId=id)
        odometry.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# Fiducial marks API
@csrf_exempt
def fiducialApi(request,id=0):
    if request.method=='GET':
        fiducial = Fiducial.objects.all()
        fiducial_serializer=FiducialSerializer(fiducial,many=True)
        return JsonResponse(fiducial_serializer.data,safe=False)
    elif request.method=='POST':
        fiducial_data=JSONParser().parse(request)
        fiducial_serializer=FiducialSerializer(data=fiducial_data)
        if fiducial_serializer.is_valid():
            fiducial_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        fiducial_data=JSONParser().parse(request)
        fiducial=Fiducial.objects.get(FiducialId=fiducial_data['FiducialId'])
        fiducial_serializer=FiducialSerializer(fiducial,data=fiducial_data)
        if fiducial_serializer.is_valid():
            fiducial_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        fiducial=Fiducial.objects.get(FiducialId=id)
        fiducial.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# Gyroscope API
@csrf_exempt
def gyroscopeApi(request,id=0):
    if request.method=='GET':
        gyroscope = Gyroscope.objects.all()
        gyroscope_serializer=GyroscopeSerializer(gyroscope,many=True)
        return JsonResponse(gyroscope_serializer.data,safe=False)
    elif request.method=='POST':
        gyroscope_data=JSONParser().parse(request)
        gyroscope_serializer=GyroscopeSerializer(data=gyroscope_data)
        if gyroscope_serializer.is_valid():
            gyroscope_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        gyroscope_data=JSONParser().parse(request)
        gyroscope=Gyroscope.objects.get(GyroscopeId=gyroscope_data['GyroscopeId'])
        gyroscope_serializer=GyroscopeSerializer(gyroscope,data=gyroscope_data)
        if gyroscope_serializer.is_valid():
            gyroscope_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        gyroscope=Gyroscope.objects.get(GyroscopeId=id)
        gyroscope.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# Global position API
@csrf_exempt
def globalpositionApi(request,id=0):
    if request.method=='GET':
        globalposition = GlobalPosition.objects.all()
        globalposition_serializer=GlobalPositionSerializer(globalposition,many=True)
        return JsonResponse(globalposition_serializer.data,safe=False)
    elif request.method=='POST':
        globalposition_data=JSONParser().parse(request)
        globalposition_serializer=GlobalPositionSerializer(data=globalposition_data)
        if globalposition_serializer.is_valid():
            globalposition_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        globalposition_data=JSONParser().parse(request)
        globalposition=GlobalPosition.objects.get(GlobalPositionId=globalposition_data['GlobalPositionId'])
        globalposition_serializer=GlobalPositionSerializer(globalposition,data=globalposition_data)
        if globalposition_serializer.is_valid():
            globalposition_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        globalposition=GlobalPosition.objects.get(GlobalPositionId=id)
        globalposition.delete()
        return JsonResponse("Deleted Successfully",safe=False)
