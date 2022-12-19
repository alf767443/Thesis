from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from pymongo import MongoClient

from MotorApplication.models import *
from MotorApplication.serializers import *

from django.core.files.storage import default_storage

PositionDB = MongoClient('mongodb://localhost:27017/')['CeDRI_UGV']['MotorApplication_motor']

# Query table API
@csrf_exempt
def tableApi(request,query=''):
    if request.method=='GET':
        result = PositionDB.aggregate([
            {
                '$sort': {
                    'dateTime': -1
                }
            }, {
                '$project': {
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
def  motorApi(request,id=0):
    if request.method=='GET':
        motor =  Motor.objects.all()
        motor_serializer= MotorSerializer( motor,many=True)
        return JsonResponse(motor_serializer.data,safe=False)
    elif request.method=='POST':
        motor_data=JSONParser().parse(request)
        motor_serializer= MotorSerializer(data= motor_data)
        if motor_serializer.is_valid():
            motor_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        motor_data=JSONParser().parse(request)
        motor= Motor.objects.get( MotorId= motor_data[' MotorId'])
        motor_serializer= MotorSerializer( motor,data= motor_data)
        if motor_serializer.is_valid():
            motor_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        motor= Motor.objects.get( MotorId=id)
        motor.delete()
        return JsonResponse("Deleted Successfully",safe=False)
