from django.shortcuts import render
from nutrition.models import Meal, UserMeal
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
    form = UserMealForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('meals')