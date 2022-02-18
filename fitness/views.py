from django.shortcuts import render, redirect
from django.views import View
from .forms import MyUserCreationForm
from django.http import HttpResponse
# fitness.models import User, Exercise, Equipment, Muscle
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def register_request(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('homepage')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = MyUserCreationForm()
    return render(request=request, template_name='register.html', context={'register_form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {email}.')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid email or password')
    form = AuthenticationForm()
    return render(request=request, template_name='registration/login.html', context={'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('homepage')


def homepage(request):
    return render(request=request, template_name='home.html')


class LoginView(View):

    def get(self, request):
        return render(request, "../registration/../templates/login.html")

    def post(self, request):
        return render(request, "../registration/../templates/login.html")


class MyUserView(View):

    def get(self, request):

        return render(request, "register.html")

    def new_user(self, request):

        return render(request, "register.html")

    def delete_user(self, user_id):
        return None


class MainView(View):

    def get(self, request):
        return render(request, "base.html")

