from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    electricityConsume = models.IntegerField(max_length=32)
    details = models.CharField(max_length=100)
    ddl = models.DateTimeField
