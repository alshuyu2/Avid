from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser, UserExercise
from .models import Image


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
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=60)

    class Meta:
        model = MyUser
        fields = ('email', 'name')

        def save(self, commit=True):
            user = super(MyUserChangeForm).save(commit=False)
            user.email = self.cleaned_data['email']
            user.name = self.cleaned_data['name']
            if commit:
                user.save()
            return user

        # ('name', 'height_in_inches', "weight_in_pounds", 'age', 'sex')


class UserExerciseForm(forms.ModelForm):

    class Meta:
        model = UserExercise
        fields = ('user', 'exercise', 'reps')

        def save(self):
            newExercise = UserExercise(user=self.cleaned_data['user'], exercise=self.cleaned_data['exercise'],
                                       reps=self.cleaned_data['reps'])
            newExercise.save()


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
