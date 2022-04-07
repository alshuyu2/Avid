# Generated by Django 4.0.2 on 2022-04-07 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('calories', models.IntegerField(null=True)),
                ('protein', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('carbs', models.IntegerField(null=True)),
                ('serving_size', models.IntegerField()),
                ('serving_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servings', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='FoodDictionary',
        ),
    ]