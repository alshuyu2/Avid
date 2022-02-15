from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')

class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('username', 'name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')

