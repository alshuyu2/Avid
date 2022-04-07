from django.contrib import admin
from .models import Exercise, Equipment, Muscle, UserExercise
from nutrition.models import Meal, UserMeal
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('email', 'name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # list_display = ['name', 'height_in_inches', "weight_in_pounds", 'age', 'sex']

# Register your models here.


admin.site.register(MyUser, MyUserAdmin)
# admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(UserExercise)
admin.site.register(Equipment)
admin.site.register(Muscle)
admin.site.register(Meal)
admin.site.register(UserMeal)



