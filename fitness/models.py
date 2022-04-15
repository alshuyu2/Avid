from __future__ import unicode_literals
from django.db import models
from users.models import MyUser


class Exercise(models.Model):
    name = models.CharField(max_length=50, null=True)
    calories = models.IntegerField(null=True)
    equipment = models.CharField(max_length=50, null=True)
    muscle = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    image = models.CharField(max_length=500, null=True)
    # video = models.URLField()

    @staticmethod
    def create_ex(name, calories, equipment, image, muscle, description):
        temp = Exercise(name=name, calories=calories, equipment=equipment,
                        muscle=muscle, image=image, description=description)
        temp.save()


# allows personalization and security to excercise and meals
class UserExercise(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    reps = models.IntegerField(null=True)


class Equipment(models.Model):
    name = models.CharField(max_length=50, null=True)


class Muscle(models.Model):
    name = models.CharField(max_length=50, null=True)


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

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
