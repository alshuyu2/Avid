# Generated by Django 4.0.2 on 2022-04-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightgraphtracker',
            name='day',
            field=models.ManyToManyField(to='fitness.Date'),
        ),
        migrations.AlterField(
            model_name='weightgraphtracker',
            name='weight',
            field=models.ManyToManyField(to='fitness.Weight'),
        ),
    ]
