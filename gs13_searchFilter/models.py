from django.db import models


# Create your models here.
class std(models.Model):
    name=models.CharField(max_length=10)
    roll=models.IntegerField()
    city=models.CharField(max_length=10)

    