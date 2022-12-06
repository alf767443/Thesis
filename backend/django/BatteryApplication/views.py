from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BatteryApplication.models import *
from BatteryApplication.serializers import *

from django.core.files.storage import default_storage

from backend.class_readURL import *

# Create your views here.

@csrf_exempt
def physicalApi(request,id=0):
    if request.method=='GET':
        physical = Physical.objects.all()
        physical_serializer=PhysicalSerializer(physical,many=True)
        return JsonResponse(physical_serializer.data,safe=False)
    elif request.method=='POST':
        physical_data=JSONParser().parse(request)
        physical_serializer=PhysicalSerializer(data=physical_data)
        if physical_serializer.is_valid():
            physical_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        physical_data=JSONParser().parse(request)
        physical=Physical.objects.get(PhysicalId=physical_data['PhysicalId'])
        physical_serializer=PhysicalSerializer(physical,data=physical_data)
        if physical_serializer.is_valid():
            physical_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        physical=Physical.objects.get(PhysicalId=id)
        physical.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    elif request.method=='LAST':
        physical=Physical.objects.last()
        physical_serializer=PhysicalSerializer(physical, many=False)
        return JsonResponse(physical_serializer.data,safe=False)


@csrf_exempt
def statusApi(request,id=0):
    if request.method=='GET':
        status = Status.objects.all()
        status_serializer=StatusSerializer(status,many=True)
        return JsonResponse(status_serializer.data,safe=False)
    elif request.method=='POST':
        status_data=JSONParser().parse(request)
        status_serializer=StatusSerializer(data=status_data)
        if status_serializer.is_valid():
            status_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        status_data=JSONParser().parse(request)
        status=Status.objects.get(StatusId=status_data['StatusId'])
        status_serializer=StatusSerializer(status,data=status_data)
        if status_serializer.is_valid():
            status_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        status=Status.objects.get(StatusId=id)
        status.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    elif request.method=='LAST':
        status=Status.objects.last()
        status_serializer=StatusSerializer(status, many=False)
        return JsonResponse(status_serializer.data,safe=False)

@csrf_exempt
def lastStatusApi(request,id=0):
    if request.method=='GET':
        status=Status.objects.last()
        status_serializer=StatusSerializer(status, many=False)
        return JsonResponse(status_serializer.data,safe=False)
        
@csrf_exempt
def sensorApi(request,id=0):
    if request.method=='GET':
        sensor = Sensor.objects.all()
        sensor_serializer=SensorSerializer(sensor,many=True)
        return JsonResponse(sensor_serializer.data,safe=False)
    elif request.method=='POST':
        sensor_data=JSONParser().parse(request)
        sensor_serializer=SensorSerializer(data=sensor_data)
        if sensor_serializer.is_valid():
            sensor_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        sensor_data=JSONParser().parse(request)
        sensor=Sensor.objects.get(SensorId=sensor_data['SensorId'])
        sensor_serializer=SensorSerializer(sensor,data=sensor_data)
        if sensor_serializer.is_valid():
            sensor_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        sensor=Sensor.objects.get(SensorId=id)
        sensor.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    elif request.method=='LAST':
        sensor=Sensor.objects.last()
        sensor_serializer=SensorSerializer(sensor, many=False)
        return JsonResponse(sensor_serializer.data,safe=False)

      
@csrf_exempt
def calculateApi(request,id=0):
    if request.method=='GET':
        calculate = Calculate.objects.all()
        calculate_serializer=CalculateSerializer(calculate,many=True)
        return JsonResponse(calculate_serializer.data,safe=False)
    elif request.method=='POST':
        calculate_data=JSONParser().parse(request)
        calculate_serializer=CalculateSerializer(data=calculate_data)
        if calculate_serializer.is_valid():
            calculate_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        calculate_data=JSONParser().parse(request)
        calculate=Calculate.objects.get(CalculateId=calculate_data['CalculateId'])
        calculate_serializer=CalculateSerializer(calculate,data=calculate_data)
        if calculate_serializer.is_valid():
            calculate_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        calculate=Calculate.objects.get(CalculateId=id)
        calculate.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    elif request.method=='LAST':
        calculate=Calculate.objects.last()
        calculate_serializer=CalculateSerializer(calculate, many=False)
        return JsonResponse(calculate_serializer.data,safe=False)


@csrf_exempt
def batteryApi(request,id=0):
    if request.method=='GET':
        battery = Battery.objects.all()
        battery_serializer=BatterySerializer(battery,many=True)
        return JsonResponse(battery_serializer.data,safe=False)
    elif request.method=='POST':
        battery_data=JSONParser().parse(request)
        battery_serializer=BatterySerializer(data=battery_data)
        if battery_serializer.is_valid():
            battery_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        battery_data=JSONParser().parse(request)
        battery=Battery.objects.get(BatteryId=battery_data['BatteryId'])
        battery_serializer=BatterySerializer(battery,data=battery_data)
        if battery_serializer.is_valid():
            battery_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        battery=Battery.objects.get(BatteryId=id)
        battery.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    elif request.method=='LAST':
        battery=Battery.objects.last()
        battery_serializer=BatterySerializer(battery, many=False)
        return JsonResponse(battery_serializer.data,safe=False)