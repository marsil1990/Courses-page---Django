# Generated by Django 5.0.2 on 2024-04-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_remove_tocomplete_exercise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise_passed',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
