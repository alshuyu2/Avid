from django import forms
from .models import UserMeal, Meal


class UserMealForm(forms.ModelForm):

    # user = forms.ModelChoiceField(queryset=MyUser.objects.all())
    # meal = forms.ModelChoiceField(queryset=Meal.objects.all())
    # servings = forms.IntegerField(required=True)

    class Meta:
        model = UserMeal
        fields = ('user', 'meal', 'servings', 'protein', 'fat', 'calories', 'carbs')

        def save(self):
            newMeal = UserMeal(user=self.cleaned_data['user'], meal=self.cleaned_data['meal'],
                               servings=self.cleaned_data['serving_size'], protein=self.cleaned_data['protein'],
                               fat=self.cleaned_data['fat'], calories=self.cleaned_data['calories'],
                               carbs=self.cleaned_data['carbs'])
            newMeal.save()
