# Generated by Django 5.0.2 on 2024-04-24 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_alter_exercise_passed_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_passed',
            old_name='id',
            new_name='key',
        ),
    ]