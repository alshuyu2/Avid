from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
# fitness.models import User, Exercise, Equipment, Muscle
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login

import datetime

# Create your views here.


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        return render(request, "login.html")


class MyUserView(View):

    def get(self, request):

        return render(request, "createUser.html")

    def new_user(self, request):

        return render(request, "createUser.html")

    def delete_user(self, user_id):
        return None


class MainView(View):

    def get(self, request):
        return render(request, "base.html")

