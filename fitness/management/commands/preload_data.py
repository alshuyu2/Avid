from django.core.management.base import BaseCommand
from fitness.models import Exercise
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        list_of_exercises = [("Push-up", 100, "None", "None", "media/images/pushup.jpg","This is the description for Push-up"),
            ("Bicep Curl", 100, "None", "None","media/images/bicepcurl.jpg","This is the description for Bicep Curl"),
            ("Cobra Exercise", 100, "None", "None", "media/images/cobra_exercise.jpg", "This is the description for Cobra Exercise"),
            ("Chest Press", 100, "None", "None", "media/images/chest_press.jpg", "This is the description for Chest Press"),
            ("Front Squat", 100, "None", "None", "media/images/front_squat.jpg", "This is the description for Front Squat"),
            ("Bent Knee Push-up", 100, "None", "None","media/images/bent_knee_pushup.jpg","This is the description for Bent Knee Push-up")]
        for arguments in list_of_exercises:
            Exercise.create_ex(*arguments)

        list_of_users = [
            ("sam", "stom@tom.com", "sam"),
            ("admin", "admin@ad.min", "admin"),
            ("tom", "tom@tom.tom", "tom"),
        ]
        userModel = get_user_model()
        for arg in list_of_users:
            newUser = userModel.objects.create_user(name=arg[0], email=arg[1], password=arg[2])
            newUser.is_superuser = True
            newUser.is_staff = True
            newUser.save()
