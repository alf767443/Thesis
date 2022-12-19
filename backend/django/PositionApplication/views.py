from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from pymongo import MongoClient

from PositionApplication.models import *
from PositionApplication.serializers import *

from django.core.files.storage import default_storage

PositionDB = MongoClient('mongodb://localhost:27017/')['CeDRI_UGV']['PositionApplication_position']

# Global position API
@csrf_exempt
def globalpositionApi(request,id=0):
    if request.method=='GET':
        result = PositionDB.aggregate([
            {
                '$sort': {
                    'dateTime': -1
                }
            }, {
                '$project': {
                    'GlobalPosition': 1
                }
            }, {
                '$unset': [
                    '_id', 'GlobalPosition._id'
                ]
            }
        ])
        result = list(result)
        return JsonResponse(result,safe=False)

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
