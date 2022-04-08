# Generated by Django 4.0.2 on 2022-04-07 18:17

from django.db import migrations
from django.contrib.auth.hashers import make_password as pw_hash
from fitness.models import MyUser, Exercise


def add_superuser(a, b):
    a = MyUser(name='admin', email='admin@admin.com', password=pw_hash('admin'), is_staff=True, is_superuser=True)
    a.save()


def add_exercise(a, b):
    ex1 = Exercise.create_ex("Bird Dog", 100, "None", "None",
                             "media/images/birddog.jpg",
                             "This is the description for birddog")
    ex2 = Exercise.create_ex("Forward Lunge ", 200, "None", "None",
                             "media/images/forward_lunge.jpg",
                             "This is the description for forward lunge")
    ex3 = Exercise.create_ex("Ankle Flexion", 300, "None", "None",
                             "media/images/ankle_flexion.jpg",
                             "This is the description for ankle flexion")


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_superuser)
    ]
