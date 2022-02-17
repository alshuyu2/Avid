from django.contrib import admin
from .models import Exercise, Equipment, Muscle

from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'name', 'height_in_inches', "weight_in_pounds", 'age', 'sex']

# Register your models here.


admin.site.register(MyUser, MyUserAdmin)
# admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Equipment)
admin.site.register(Muscle)



