from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ('email',)
        # ('name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')

        def save(self, commit=True):
            user = super(MyUserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('email',)
        # ('name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')

