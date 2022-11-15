from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BatteryApplication.models import Charge, Status
from BatteryApplication.serializers import ChargeSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def chargeApi(request,id=0):
    if request.method=='GET':
        charge = Charge.objects.all()
        charge_serializer=ChargeSerializer(charge,many=True)
        return JsonResponse(charge_serializer.data,safe=False)
    elif request.method=='POST':
        charge_data=JSONParser().parse(request)
        charge_serializer=ChargeSerializer(data=charge_data)
        if charge_serializer.is_valid():
            charge_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        charge_data=JSONParser().parse(request)
        charge=Charge.objects.get(ChargeId=charge_data['ChargeId'])
        charge_serializer=ChargeSerializer(charge,data=charge_data)
        if charge_serializer.is_valid():
            charge_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        charge=Charge.objects.get(ChargeId=id)
        charge.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)