from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import CustomUserManager
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractBaseUser, PermissionsMixin):
    # username = None
    email = models.EmailField(_('email address'), unique=True)

    name = models.CharField(_('name'), max_length=30, blank=True)

    is_staff = models.BooleanField(_('staff'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    sex = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    height_in_inches = models.IntegerField(default=0, null=True)
    weight_in_pounds = models.IntegerField(default=0, null=True)
    age = models.IntegerField(default=0, null=True)

    profile_picture = models.ImageField(default='media/images/Blank_profile.jpg', upload_to='profile_pics')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('myUser')
        verbose_name_plural = _('myUsers')

    def get_name(self):
        return self.name

    # name = models.CharField(max_length=60)
    # height_in_inches = models.IntegerField()
    # weight_in_pounds = models.IntegerField()
    # age = models.IntegerField()
    # sex = models.BooleanField()

    def __str__(self):
        return self.email


class Exercise(models.Model):
    name = models.CharField(max_length=50, null=True)
    id = models.IntegerField(primary_key=True)
    calories = models.IntegerField(null=True)
    equipment = models.ManyToManyField('Equipment')
    muscle = models.ManyToManyField('Muscle')
    description = models.CharField(max_length=1000, null=True)
    # Undecided
    # image = models.ImageField()
    # video = models.URLField()


class Equipment(models.Model):
    name = models.CharField(max_length=50, null=True)


class Muscle(models.Model):
    name = models.CharField(max_length=50, null=True)


class WeightGraphTracker(models.Model):
    name = models.CharField(max_length=50)
    weight = models.ManyToManyField('Weight')
    day = models.ManyToManyField('Date')

    def __str__(self):
        return self.name


class Weight(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Date(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
