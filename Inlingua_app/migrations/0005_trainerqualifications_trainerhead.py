# Generated by Django 5.0.6 on 2024-07-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0004_trainer_trainerqualifications_trainingbatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerqualifications',
            name='trainerHead',
            field=models.BooleanField(default=False),
        ),
    ]