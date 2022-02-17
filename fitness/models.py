from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass
    name = models.CharField(max_length=60)
    height_in_inches = models.IntegerField()
    weight_in_pounds = models.IntegerField()
    age = models.IntegerField()
    sex = models.BooleanField()

    def __str__(self):
        return self.username


class Exercise(models.Model):
    name = models.CharField(max_length=50, null=True)
    id = models.IntegerField(primary_key=True)
    calories = models.IntegerField(null=True)
    equipment = models.ManyToManyField('Equipment')
    muscle = models.ManyToManyField('Muscle')
    description = models.CharField(max_length=1000, null=True)
    # Undecided
    # image = models.ImageField()
    # video = models.URLField()


class Equipment(models.Model):
    name = models.CharField(max_length=50,null=True)


class Muscle(models.Model):
    name = models.CharField(max_length=50,null=True)


class WeightGraphTracker(models.Model):
    name = models.CharField(max_length=50)
    weight = models.ManyToManyField('Weight')
    day = models.ManyToManyField('Date')

    def __str__(self):
        return self.name


class Weight(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Date(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
