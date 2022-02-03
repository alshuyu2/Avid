from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):
    name = models.CharField(max_length=60)
    height_in_inches = models.IntegerField(max_length=3)
    weight_in_pounds = models.IntegerField(max_length=3)
    age = models.IntegerField(max_length=3)
    sex = models.BooleanField()