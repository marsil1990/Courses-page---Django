from django.contrib import admin

# Register your models here.
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ('name', 'subject', 'difficulty', 'description', 'creation_date')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'subject',)
    readonly_fields = ('creation_date',)