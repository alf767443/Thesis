from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BatteryApplication.models import Physical, Status
from BatteryApplication.serializers import PhysicalSerializer,StatusSerializer

from django.core.files.storage import default_storage

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

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)