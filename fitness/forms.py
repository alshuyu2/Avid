from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=60)

    class Meta:
        model = MyUser
        fields = ('email', 'name')
        # ('name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')

        def save(self, commit=True):
            user = super(MyUserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.name = self.cleaned_data['name']
            if commit:
                user.save()
            return user


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('email',)
        # ('name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')

