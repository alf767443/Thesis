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

database = MongoClient('mongodb://localhost:27017/')['CeDRI_UGV']['BatteryApplication_battery']

# Query table API
@csrf_exempt
def tableApi(request,query=''):
    if request.method=='GET':
        result = database.aggregate([
            {
                '$sort': {
                    'dateTime': -1
                }
            }, {
                '$project': {
                    'dateTime': 1,
                    query: 1
                }
            }, {
                '$unset': [
                    '_id', query+'._id'
                ]
            }
        ])
        result = list(result)
        return JsonResponse(result,safe=False)



# Full database
@csrf_exempt
def batteryApi(request,id=0):
    if request.method=='GET':
        result = database.aggregate([
            {
                '$sort': {
                    'dateTime': -1
                }
            }, {
                '$unset': [
                    '_id'
                ]
            }
        ])
        result = list(result)
        return JsonResponse(result,safe=False)
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

# Query
@csrf_exempt
def queryApi(request,query=0):
    if request.method=='GET':
        # First item of battery db
        if query == '1':
            result = database.aggregate([
                {
                    '$unset': [
                        '_id'
                    ]
                },
                {
                    '$sort': {
                        'dateTime': -1
                    }
                },
                {
                    '$limit': 1
                }
            ])
            result = list(result)  
        # Plot percent by time 
        elif query == '2':
            result = database.aggregate([
                {
                    '$project': {
                        'Calculate': 1, 
                        'Sensor': 1, 
                        'dateTime': {
                            '$dateTrunc': {
                                'date': '$dateTime', 
                                'unit': 'minute'
                            }
                        }
                    }
                }, {
                    '$addFields': {
                        'Status': '$Calculate.Status', 
                        'Percent': {
                            '$multiply': [
                                '$Calculate.Percent', 100
                            ]
                        }
                    }
                }, {
                    '$unset': [
                        '_id', 'Sensor', 'Calculate'
                    ]
                }, {
                    '$densify': {
                        'field': 'dateTime', 
                        'range': {
                            'step': 1, 
                            'unit': 'minute', 
                            'bounds': 'full'
                        }
                    }
                }, {
                    '$group': {
                        '_id': '$dateTime', 
                        'dateTime': {
                            '$first': '$dateTime'
                        }, 
                        'Percent': {
                            '$avg': '$Percent'
                        }, 
                        'Status': {
                            '$first': '$Status'
                        }, 
                        'count': {
                            '$sum': 1
                        }
                    }
                }, {'$set': {
                        'Percent': {'$round': ['$Percent',3]}
                    }
                }, {
                    '$sort': {
                        'dateTime': -1
                    }
                }, {
                    '$limit': 4320
                }, {
                    '$sort': {
                        'dateTime': 1
                    }
                }
            ])
            result = list(result)  
        else:
            result = "No query was setting"
        return JsonResponse(result,safe=False)