from djongo import models as models

# Create your models here.
class Administrator(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    dateTime = models.DateTimeField(auto_created=True, auto_now_add=True)
    Decision = models.CharField(max_length=1)
    Priority = models.CharField(max_length=1)

    def __unicode__(self):
        return self._id
    
    objects = models.DjongoManager()
    
class Remote(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    dateTime = models.DateTimeField(auto_created=True, auto_now_add=True)
    Decision = models.CharField(max_length=1)
    Priority = models.CharField(max_length=1)

    def __unicode__(self):
        return self._id
    
    objects = models.DjongoManager()

class Robot(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    dateTime = models.DateTimeField(auto_created=True, auto_now_add=True)
    Decision = models.CharField(max_length=1)
    Priority = models.CharField(max_length=1)

    def __unicode__(self):
        return self._id

    objects = models.DjongoManager()