from django.contrib import admin

# Register your models here.

from .models import Lesson

@admin.register(Lesson)
class Exercise_passedAdmin(admin.ModelAdmin):
    list_display= ('id','order', 'topic', 'numberOfEcercises', 'course')
    list_filter = ('id','order')
    search_fields = ('id', 'order',)