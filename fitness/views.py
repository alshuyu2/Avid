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
        return render(request, "base.html")

    def post(self, request):
        return None


def log_out(request):
    return None
