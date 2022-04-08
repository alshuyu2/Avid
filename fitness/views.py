from django.shortcuts import render, redirect
from django.views import View
from .forms import MyUserCreationForm, MyUserChangeForm
from django.http import HttpResponse
from fitness.models import MyUser
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import ImageForm, UserExerciseForm
from .models import Exercise, UserExercise, Equipment, Muscle

# Create your views here.


def register_request(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('homepage')
        messages.error(request, 'Unsuccessful registration.')
        messages.error(request, form.errors)

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
                return redirect('userpage')
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


def userpage(request):
    return render(request=request, template_name='userpage.html')


def settings(request):
    return render(request=request, template_name='settings.html')


def about(request):
    return render(request=request, template_name='about.html')


def edit_user(request):
    User = request.user
    if request.method == 'POST':
        User.name = request.POST['name']
        User.height_in_inches = request.POST['height_in_inches']
        User.weight_in_pounds = request.POST['weight_in_pounds']
        if request.POST['sex'] == 'male':
            User.sex = True
        else:
            User.sex = False
        User.age = request.POST['age']
        User.save()
        messages.error(request, 'Successfully Updated Profile')
    return render(request=request, template_name='settings.html')


def image_upload_view(request):
    """Process images uploaded by users"""
    User = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'settings.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

# unfinished

# class RoutinePage(View):
#     def get(self, request):
#         if request.session.get("username"):
#             return render(request, "routine.html")
#         return render(request, 'registration/login.html')
#
#     def post(self, request):
#         name = request.Post['name']


# display exercise detail in another page
def exercise_main(request):
    Exercises = list(Exercise.objects.all().values())
    print(Exercises)
    tmp = list(UserExercise.objects.all())
    Userexercises = []
    for i in tmp:
        if i.user == request.user:
            Userexercises.append(i)
    print(Userexercises)
    return render(request=request, template_name='exercise_main.html', context={"exercises": Exercises,
                                                                                "userexercises": Userexercises})


def exercise_add(request):
    Exercises = list(Exercise.objects.all())
    con = 0

    if request.method == 'POST':
        form = UserExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('exercise_main')
    for i in Exercises:
        if request.GET['exercise'] in i.name:
            con = i
    return render(request=request, template_name="exercise_add.html", context={"exercise": con,
                                                                               "exercises": Exercises})


def catalog(request):
    return render(request, template_name='recommendpage.html', context={"exercise": Exercise.objects.all()})

