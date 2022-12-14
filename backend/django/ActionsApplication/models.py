from django.db import models

# Create your models here
class Actions(models.Model):
    ActionsId = models.AutoField(primary_key=True)
    ActionsAction = models.IntegerField()
    ActionsStatus = models.IntegerField()
    ActionsPriority = models.IntegerField()
    ActionsSource = models.IntegerField()

class Queue(models.Model):
    QueueId = models.AutoField(primary_key=True)
    QueueStatus = models.IntegerField()
    ActionsId = models.IntegerField()
