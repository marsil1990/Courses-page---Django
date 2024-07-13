# Generated by Django 5.0.2 on 2024-05-30 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_rename_id_exercise_passed_key'),
        ('lessons', '0002_alter_lesson_id_alter_lesson_numberofecercises'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseMultipleOption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('url_video', models.URLField(blank=True)),
                ('phrase_multiple_option', models.TextField(blank=True)),
                ('answers_multiple_option', models.TextField(blank=True)),
                ('answer_correct_multiOption', models.CharField(blank=True, max_length=50)),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise_options',
            fields=[
                ('exerciseMultipleOption', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='options', serialize=False, to='exercises.exercisemultipleoption')),
                ('answer_option', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='exercise_passed',
            name='exercise',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exercises.exercisemultipleoption'),
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]
