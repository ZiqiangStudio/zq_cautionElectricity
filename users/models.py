from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.IntegerField()
    electricity = models.IntegerField()
    # 与items有一个one to many关系
    completedItems = models.IntegerField()
    shutDownCount = models.IntegerField()
