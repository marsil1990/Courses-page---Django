# Generated by Django 5.0.2 on 2024-05-30 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0013_delete_exercise_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_option', models.CharField(max_length=100)),
                ('exerciseMultipleOption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='exercises.exercisemultipleoption')),
            ],
        ),
    ]
