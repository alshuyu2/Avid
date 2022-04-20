from django.db import models
from django.db import migrations
# Create your models here.

# What data should the nutrition model have?

# It should have calories
# It should have calorie tracking
# It should have the daily average vitamin requirements
# It should have the option to add your own custom food
# You can have a food model
# You can have a diet tracking model

# For now  have a simple food model called food dictionary model that has all the necessary food items
from fitness.models import MyUser


class Meal(models.Model):
    # user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    serving_size = models.IntegerField()
    serving_unit = models.CharField(max_length=50)  # example: ounce, unit

    @staticmethod
    def create_meal(name, calories, protein, fat, carbs, serving_size, serving_unit):
        temp = Meal(name=name, calories=calories, protein=protein, fat=fat,
                    carbs=carbs, serving_size=serving_size, serving_unit=serving_unit)
        temp.save()


class UserMeal(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    servings = models.IntegerField()
    calories = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    carbs = models.IntegerField(null=True)

