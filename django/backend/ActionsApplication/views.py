from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ActionsApplication.models import *
from ActionsApplication.serializers import *

from django.core.files.storage import default_storage

# Actions API
@csrf_exempt
def actionsApi(request,id=0):
    if request.method=='GET':
        actions = Actions.objects.all()
        actions_serializer=ActionsSerializer(actions,many=True)
        return JsonResponse(actions_serializer.data,safe=False)
    elif request.method=='POST':
        actions_data=JSONParser().parse(request)
        actions_serializer=ActionsSerializer(data=actions_data)
        if actions_serializer.is_valid():
            actions_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        actions_data=JSONParser().parse(request)
        actions=Actions.objects.get(ActionsId=actions_data['ActionsId'])
        actions_serializer=ActionsSerializer(actions,data=actions_data)
        if actions_serializer.is_valid():
            actions_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        actions=Actions.objects.get(ActionsId=id)
        actions.delete()
        return JsonResponse("Deleted Successfully",safe=False)
