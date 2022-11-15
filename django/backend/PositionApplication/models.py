from django.db import models

# Create your models here.
class Odometry(models.Model):
    OdometryId = models.AutoField(primary_key=True)
    OdometryLeft = models.BinaryField()
    OdometryRight = models.BinaryField()

class Fiducial(models.Model):
    FiducialId = models.AutoField(primary_key=True)
    FiducialMark = models.BinaryField()

class Gyroscope(models.Model):
    GyroscopeId = models.AutoField(primary_key=True)
    GyroscopeAngle = models.BinaryField()