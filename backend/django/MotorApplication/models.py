from djongo import models as models

class Voltage(models.Model):
    _id = models.ObjectIdField()
    Left = models.FloatField(blank=True, null=True)
    Right = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Current(models.Model):
    _id = models.ObjectIdField()
    Left = models.FloatField(blank=True, null=True)
    Right = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Power(models.Model):
    _id = models.ObjectIdField()
    Left = models.FloatField(blank=True, null=True)
    Right = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Motor(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    dateTime = models.DateTimeField(auto_created=True, auto_now_add=True)
    Voltage = models.EmbeddedField(model_container=Voltage, blank=True, null=True)
    Current = models.EmbeddedField(model_container=Current, blank=True, null=True)
    Power = models.EmbeddedField(model_container=Power, blank=True, null=True)

    def __unicode__(self):
        return self._id

    objects = models.DjongoManager()