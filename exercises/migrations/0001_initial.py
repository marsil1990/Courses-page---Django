# Generated by Django 5.0.2 on 2024-02-29 21:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleOption',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('url_video', models.URLField(blank=True)),
                ('phrase_multiple_option', models.TextField()),
                ('answers_multiple_option', models.TextField()),
                ('answer_correct', models.CharField(max_length=50)),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToComplete',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('url_video', models.URLField(blank=True)),
                ('phrase_complete', models.TextField()),
                ('words_complete', models.TextField()),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exercise_passed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('multiple_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.multipleoption')),
                ('to_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.tocomplete')),
            ],
        ),
    ]