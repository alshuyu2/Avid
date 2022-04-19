from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, password, **extra_fields):
        if not name:
            raise ValueError('The name must be set')
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)

    def create_superuser(self, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_superuser=True.'))
        return self._create_user(name, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'), unique=True)

    name = models.CharField(gettext_lazy('name'), max_length=30, unique=True)

    is_staff = models.BooleanField(gettext_lazy('staff'), default=False)
    is_active = models.BooleanField(gettext_lazy('active'), default=True)
    sex = models.BooleanField(default=False)

    date_joined = models.DateTimeField(gettext_lazy('date joined'), auto_now_add=True)

    height_in_inches = models.IntegerField(default=0, null=True)
    weight_in_pounds = models.IntegerField(default=0, null=True)
    age = models.IntegerField(default=0, null=True)

    profile_picture = models.ImageField(default='media/images/Blank_profile.jpg', upload_to='profile_pics')

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = gettext_lazy('myUser')
        verbose_name_plural = gettext_lazy('myUsers')

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name
