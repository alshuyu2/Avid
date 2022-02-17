from django.shortcuts import render, redirect
from django.views import View
# fitness.models import User, Exercise, Equipment, Muscle
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Create your views here.

class LoginView(View):

    def get(self, request):
        # go to the login page for now
        path = {request.path}
        if path == "/home/":
            return render(request, "base.html")
        else:
            return render(request, "login.html")

    def post(self, request):
        #request.POST["name"]

        return render(request, "base.html")


def log_out(request):
    return None

class my_User(View):

    def new_user(self, name, height, weight, age, sex):
        return None

    def delete_user(self, user_id):
        return None