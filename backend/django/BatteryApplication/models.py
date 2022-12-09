
#from django.db import models
from djongo import models as models

# Create your models here.
class Sensor(models.Model):
    _id         = models.ObjectIdField(primary_key=True)
    Voltage     = models.FloatField(blank=True, null=True)
    Current     = models.FloatField(blank=True, null=True)
    Temperature = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        

class Calculate(models.Model):
    _id         = models.ObjectIdField(primary_key=True)
    Status      = models.CharField(max_length=2, blank=True, null=True)
    Percent     = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False

class Battery(models.Model):
    _id         = models.ObjectIdField()
    dateTime    = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True, null=True)
    Sensor      = models.EmbeddedField(model_container=Sensor, blank=True, null=True)
    Calculate   = models.EmbeddedField(model_container=Calculate, blank=True, null=True)

    objects = models.DjongoManager()