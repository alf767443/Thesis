from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer

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

@csrf_exempt
def queueApi(request,id=0):
    if request.method=='GET':
        queue = Queue.objects.all()
        queue_serializer=QueueSerializer(queue,many=True)
        return JsonResponse(queue_serializer.data,safe=False)
    elif request.method=='POST':
        queue_data=JSONParser().parse(request)
        queue_serializer=QueueSerializer(data=queue_data)
        if queue_serializer.is_valid():
            queue_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        queue_data=JSONParser().parse(request)
        queue=Queue.objects.get(QueueId=queue_data['QueueId'])
        queue_serializer=QueueSerializer(queue,data=queue_data)
        if queue_serializer.is_valid():
            queue_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        queue=Queue.objects.get(QueueId=id)
        queue.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def actionsQueueApi(request,id=0):
    if request.method=='GET':
        actions = Actions.objects.all()
        #Do or cancelled
        actionsDo = actions.filter(ActionsStatus__in=['1'])
        actionsDo_serializer = ActionsSerializer(actionsDo,many=True)
        #ToDo
        actionsToDo = actions.filter(ActionsStatus='0')
        actionsToDo_serializer = ActionsSerializer(actionsDo,many=True)

        actions_serializer=ActionsSerializer(actions,many=True)
        teste = JSONRenderer().render(actions_serializer.data)
        print(teste)
        
        return JsonResponse(actionsDo_serializer.data,safe=False)