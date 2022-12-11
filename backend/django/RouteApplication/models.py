from djongo import models as models
from PositionApplication.models import Position


# Create your models here.
class Data(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    Distance = models.FloatField(blank=True, null=True)
    Consumption = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Route(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    dateTime    = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True, null=True)
    Estimated = models.EmbeddedField(model_container=Data, blank=True, null=True)
    Real = models.EmbeddedField(model_container=Data, blank=True, null=True)
    StartPoint = models.OneToOneField(Position, on_delete= models.CASCADE, related_name='Start', blank=True, null=True)
    EndPoint = models.OneToOneField(Position, on_delete= models.CASCADE, related_name='End', blank=True, null=True)
    
    def __unicode__(self):
        return self._id
    
    objects = models.DjongoManager()