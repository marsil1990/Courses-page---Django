# Generated by Django 5.0.2 on 2024-03-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise_passed',
            name='message',
            field=models.CharField(default='Aproved', max_length=100),
        ),
    ]