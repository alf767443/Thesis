from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from pymongo import MongoClient
from django.http import HttpResponse
from django.core import serializers
from bson.json_util import dumps, loads

from BatteryApplication.models import *
from BatteryApplication.serializers import *

from django.core.files.storage import default_storage

from backend.class_readURL import *

# Create your views here.

client = MongoClient('mongodb://localhost:27017/')

@csrf_exempt
def sensorApi(request,id=0):
    if request.method=='GET':
        result = client['CeDRI_UGV']['BatteryApplication_battery'].aggregate([
            {
                '$sort': {
                    'dateTime': -1
                }
            }, {
                '$unset': [
                    '_id', 'Sensor._id', 'Calculate'
                ]
            }
        ])
        result = list(result)
        return JsonResponse(result,safe=False)
    elif request.method=='POST':
        sensor_data=JSONParser().parse(request)
        print(sensor_data)
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
        result = client['CeDRI_UGV']['BatteryApplication_battery'].aggregate([
            {
                '$sort': {
                    'dateTime': -1
                }
            }, {
                '$unset': [
                    '_id', 'Sensor', 'Calculate._id'
                ]
            }
        ])
        result = list(result)
        return JsonResponse(result,safe=False)
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

def last():
    
    result = client['CeDRI_UGV']['BatteryApplication_battery'].aggregate([
        {
            '$sort': {
                'dateTime': -1
            }
        }, {
            '$limit': 1
        }
    ])
    return result