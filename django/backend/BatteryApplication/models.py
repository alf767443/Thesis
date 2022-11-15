from django.db import models

# Create your models here.
class Charge(models.Model):
    ChargeId = models.AutoField(primary_key=True)
    ChargeVoltage = models.FloatField()
    ChargePercent = models.FloatField()

class Status(models.Model):
    StatusId = models.AutoField(primary_key=True)
    StatusBattery = models.BinaryField()