from django.db import models
from users.models import User


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    electricityConsume = models.IntegerField()
    details = models.CharField(max_length=100)
    ddl = models.CharField(max_length=32, null=True)
    itemUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    isCompleted = models.BooleanField(default=False)
