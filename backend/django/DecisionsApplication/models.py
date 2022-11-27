from django.db import models

# Create your models here.
class Administrator(models.Model):
    AdministratorId = models.AutoField(primary_key=True)
    AdministratorDecision = models.IntegerField()
    AdministratorPriority = models.IntegerField()
    
class Remote(models.Model):
    RemoteId = models.AutoField(primary_key=True)
    RemoteDecision = models.IntegerField()
    RemotePriority = models.IntegerField()

class Robot(models.Model):
    RobotId = models.AutoField(primary_key=True)
    RobotDecision = models.IntegerField()
    RobotPriority = models.IntegerField()