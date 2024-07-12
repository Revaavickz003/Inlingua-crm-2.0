# Generated by Django 5.0.6 on 2024-07-11 10:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0003_rename_account_paide_studenttable_amount_paide'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_trainer_head', models.BooleanField(default=False)),
                ('languages', models.ManyToManyField(to='Inlingua_app.language')),
                ('levels', models.ManyToManyField(to='Inlingua_app.levelsandhour')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerQualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=255)),
                ('institution', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inlingua_app.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inlingua_app.trainer')),
            ],
        ),
    ]