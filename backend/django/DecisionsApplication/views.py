from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DecisionsApplication.models import *
from DecisionsApplication.serializers import *

from django.core.files.storage import default_storage

# Administrator API
@csrf_exempt
def administratorApi(request,id=0):
    if request.method=='GET':
        administrator = Administrator.objects.all()
        administrator_serializer=AdministratorSerializer(administrator,many=True)
        return JsonResponse(administrator_serializer.data,safe=False)
    elif request.method=='POST':
        administrator_data=JSONParser().parse(request)
        administrator_serializer=AdministratorSerializer(data=administrator_data)
        if administrator_serializer.is_valid():
            administrator_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        administrator_data=JSONParser().parse(request)
        administrator=Administrator.objects.get(AdministratorId=administrator_data['AdministratorId'])
        administrator_serializer=AdministratorSerializer(administrator,data=administrator_data)
        if administrator_serializer.is_valid():
            administrator_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        administrator=Administrator.objects.get(AdministratorId=id)
        administrator.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# Remote API
@csrf_exempt
def remoteApi(request,id=0):
    if request.method=='GET':
        remote = Remote.objects.all()
        remote_serializer=RemoteSerializer(remote,many=True)
        return JsonResponse(remote_serializer.data,safe=False)
    elif request.method=='POST':
        remote_data=JSONParser().parse(request)
        remote_serializer=RemoteSerializer(data=remote_data)
        if remote_serializer.is_valid():
            remote_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        remote_data=JSONParser().parse(request)
        remote=Remote.objects.get(RemoteId=remote_data['RemoteId'])
        remote_serializer=RemoteSerializer(remote,data=remote_data)
        if remote_serializer.is_valid():
            remote_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        remote=Remote.objects.get(RemoteId=id)
        remote.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# Robot API
@csrf_exempt
def robotApi(request,id=0):
    if request.method=='GET':
        robot = Robot.objects.all()
        robot_serializer=RobotSerializer(robot,many=True)
        return JsonResponse(robot_serializer.data,safe=False)
    elif request.method=='POST':
        robot_data=JSONParser().parse(request)
        robot_serializer=RobotSerializer(data=robot_data)
        if robot_serializer.is_valid():
            robot_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        robot_data=JSONParser().parse(request)
        robot=Robot.objects.get(RobotId=robot_data['RobotId'])
        robot_serializer=RobotSerializer(robot,data=robot_data)
        if robot_serializer.is_valid():
            robot_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        robot=Robot.objects.get(RobotId=id)
        robot.delete()
        return JsonResponse("Deleted Successfully",safe=False)
