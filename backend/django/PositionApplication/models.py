from djongo import models as models

class Odometry(models.Model):
    _id = models.ObjectIdField()
    Left = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    Right = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Velocity(models.Model):
    _id = models.ObjectIdField()
    Left = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    Right = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Acceleration(models.Model):
    _id = models.ObjectIdField()
    Left = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    Right = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Fiducial(models.Model):
    _id = models.ObjectIdField()
    Mark = models.CharField(max_length=1, blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class Gyroscope(models.Model):
    _id = models.ObjectIdField()
    Angle = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __unicode__(self):
        return self._id

class GlobalPosition(models.Model):
    _id = models.ObjectIdField()
    X = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    Y = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    
    class Meta:
        managed = False

    def __unicode__(self):
        return self._id

class Position(models.Model):
    _id = models.ObjectIdField()
    dateTime    = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True, null=True)
    Odometry = models.EmbeddedField(model_container=Odometry, blank=True, null=True)
    Velocity = models.EmbeddedField(model_container=Velocity, blank=True, null=True)
    Acceleration = models.EmbeddedField(model_container=Acceleration, blank=True, null=True)
    Fiducial = models.EmbeddedField(model_container=Fiducial, blank=True, null=True)
    Gyroscope = models.EmbeddedField(model_container=Gyroscope, blank=True, null=True)
    GlobalPosition = models.EmbeddedField(model_container=GlobalPosition, blank=True, null=True)

    def __unicode__(self):
        return self._id
    
    objects = models.DjongoManager()