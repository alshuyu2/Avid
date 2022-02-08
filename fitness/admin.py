from django.contrib import admin
from .models import User, Exercise, Equipment, Muscle
# Register your models here.

admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Equipment)
admin.site.register(Muscle)


