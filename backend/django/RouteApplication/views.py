from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RouteApplication.models import Route
from RouteApplication.serializers import RouteSerializer

from django.core.files.storage import default_storage

# Route API
@csrf_exempt
def routeApi(request,id=0):
    if request.method=='GET':
        route = Route.objects.all()
        route_serializer=RouteSerializer(route,many=True)
        return JsonResponse(route_serializer.data,safe=False)
    elif request.method=='POST':
        route_data=JSONParser().parse(request)
        route_serializer=RouteSerializer(data=route_data)
        if route_serializer.is_valid():
            route_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        route_data=JSONParser().parse(request)
        route=Route.objects.get(RouteId=route_data['RouteId'])
        route_serializer=RouteSerializer(route,data=route_data)
        if route_serializer.is_valid():
            route_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        route=Route.objects.get(RouteId=id)
        route.delete()
        return JsonResponse("Deleted Successfully",safe=False)
