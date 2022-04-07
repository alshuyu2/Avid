from django.db import models

# Create your models here.

#What data should the nutrition model have?

#It should have calories
#It should have calorie tracking
#It should have the daily average vitamin requirements
#It should have the option to add your own custom food
#You can have a food model
#You can have a diet tracking model

#For now  have a simple food model called food dictionary model that has all the necessary food items
class FoodDictionary(models.Model):
    #Name
    name = models.CharField(max_length=50)
    #Nutrition information (Carbohydrates, fats, protein, and all the vitamins and minerals)
    calories = models.IntegerField #start with calories for now
    #Serving size (number of the amount, lbs, grams for solid food, liter for liquid drinks)
    serving = models.IntegerField
    foodType = models.BooleanField #put true if it's solid, false if it's liquid


class Meal(models.Model):
    # user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    calories = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    carbs = models.IntegerField(null=True)
    serving_size = models.CharField(max_length=50, null=True)


class UserMeal(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    servings = models.IntegerField(null=True)
