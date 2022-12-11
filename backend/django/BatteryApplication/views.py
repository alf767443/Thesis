from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from pymongo import MongoClient

from BatteryApplication.models import *
from BatteryApplication.serializers import *

from django.core.files.storage import default_storage

from backend.class_readURL import *

# Create your views here.

BatteryDB = MongoClient('mongodb://localhost:27017/')['CeDRI_UGV']['BatteryApplication_battery']

@csrf_exempt
def sensorApi(request,id=0):
    if request.method=='GET':
        result = BatteryDB.aggregate([
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
  
@csrf_exempt
def calculateApi(request,id=0):
    if request.method=='GET':
        result = BatteryDB.aggregate([
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
