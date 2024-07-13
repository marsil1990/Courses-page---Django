from django.contrib import admin

# Register your models here.

from .models import Exercise_passed, ExerciseMultipleOption, Exercise_options

@admin.register(ExerciseMultipleOption)
class ExerciseAdmin(admin.ModelAdmin):
    list_display= ('id',)
    search_fields = ('id',)
    list_filter = ('id',)

@admin.register(Exercise_options)
class Exercise_optionsAdmin(admin.ModelAdmin):
    list_display = ('exerciseMultipleOption',)
    
@admin.register(Exercise_passed)
class Exercise_passedAdmin(admin.ModelAdmin):
    list_display = ('student', 'exercise_id',)

    
    
    
