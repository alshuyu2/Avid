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


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(null=True)
    calories = models.IntegerField(null=True)
    equipment = models.ManyToManyField(Equipment)
    muscle = models.ManyToManyField(Muscle)
    description = models.CharField(max_length=1000)
    # Undecided
    # image = models.ImageField()
    # video = models.URLField()


class Equipment(models.Model):
    name = models.CharField(max_length=50)


class Muscle(models.Model):
    name = models.CharField(max_length=50)

