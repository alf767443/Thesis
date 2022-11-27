from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeesName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFieldName = models.CharField(max_length=500)