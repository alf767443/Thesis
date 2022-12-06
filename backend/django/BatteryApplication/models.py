
from django.db import models
from djongo import models as models_

# Create your models here.
class Physical(models.Model):
    PhysicalId = models.AutoField(primary_key=True)
    PhysicalVoltage = models.FloatField()
    PhysicalCurrent = models.FloatField()
    PhysicalTemperature = models.FloatField()

class Status(models.Model):
    StatusId = models.AutoField(primary_key=True)
    StatusBattery = models.IntegerField()
    StatusPercent = models.FloatField()



class Sensor(models_.Model):
    _id         = models_.ObjectIdField()
    Voltage     = models_.FloatField(blank=True, null=True)
    Current     = models_.FloatField(blank=True, null=True)
    Temperature = models_.FloatField(blank=True, null=True)


class Calculate(models_.Model):
    _id         = models_.ObjectIdField()
    Status      = models_.CharField(max_length=2, blank=True, null=True)
    Percent     = models_.FloatField(blank=True, null=True)

class Battery(models_.Model):
    _id         = models_.ObjectIdField()
    dateTime    = models_.DateTimeField(auto_created=True, auto_now_add=True, blank=True, null=True)
    Sensor      = models_.EmbeddedField(model_container=Sensor, blank=True, null=True)
    Calculate   = models_.EmbeddedField(model_container=Calculate, blank=True, null=True)

    objects = models_.DjongoManager()