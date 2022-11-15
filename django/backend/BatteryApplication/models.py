from django.db import models

# Create your models here.
class Physical(models.Model):
    PhysicalId = models.AutoField(primary_key=True)
    PhysicalVoltage = models.FloatField()
    PhysicalCurrent = models.FloatField()
    PhysicalTemperature = models.FloatField()

class Status(models.Model):
    StatusId = models.AutoField(primary_key=True)
    StatusBattery = models.BinaryField()
    StatusPercent = models.FloatField()