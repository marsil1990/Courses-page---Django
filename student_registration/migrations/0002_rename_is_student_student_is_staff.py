# Generated by Django 5.0.2 on 2024-02-29 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_student',
            new_name='is_staff',
        ),
    ]
