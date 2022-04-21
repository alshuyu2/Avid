from django.shortcuts import render, redirect
from nutrition.models import Meal, UserMeal
from .forms import UserMealForm
from .models import UserMeal, Meal


# Create your views here.
def meals(request):
    Meals = list(Meal.objects.all())
    tmp = list(UserMeal.objects.all())
    Usermeals = []
    for i in tmp:
        if i.user == request.user:
            Usermeals.append(i)
    return render(request=request, template_name='meals.html', context={"Usermeals": Usermeals,
                                                                        "Meals": Meals})


def meals_add(request):
    myPost = request.POST.copy()
    Meals = list(Meal.objects.all())
    for i in Meals:
        if i.name == myPost['meal']:
            myPost['meal'] = i.id
            myPost['protein'] = i.protein*eval(myPost['servings'])
            myPost['calories'] = i.calories*eval(myPost['servings'])
            myPost['carbs'] = i.carbs*eval(myPost['servings'])
            myPost['fat'] = i.fat*eval(myPost['servings'])
            request.POST = myPost
    form = UserMealForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('meals')
